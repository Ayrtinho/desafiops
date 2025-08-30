import os
from flask import Flask, request, render_template, send_from_directory, jsonify
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer 
import google.generativeai as genai

app = Flask(__name__)

# Configura a chave da API Google AI Studio
GOOGLE_API_KEY = "AIzaSyBKi1zBj4smXtcvVeEDy2PgEZeDDwEVWZY"

# Configura o Google AI Studio
genai.configure(api_key=GOOGLE_API_KEY)

# Baixa os recursos necessários do NLTK apenas se não existirem
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('rslp', quiet=True)

def extract_text(file_storage):
    filename = file_storage.filename
    if filename.endswith('.txt'):
        return file_storage.read().decode('utf-8')
    elif filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file_storage)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        raise ValueError("Formato de arquivo não suportado.")

def preprocess_text(text):
    stop_words = set(stopwords.words('portuguese'))
    stemmer = RSLPStemmer()
    
    # Usa o tokenizer padrão do NLTK sem especificar idioma
    try:
        tokens = nltk.word_tokenize(text.lower())
    except:
        # Fallback simples se o tokenizer falhar
        tokens = text.lower().split()
    
    # Usa RSLPStemmer que é específico para português
    filtered = [stemmer.stem(w) for w in tokens if w.isalpha() and w not in stop_words]
    return ' '.join(filtered)

def classify_and_respond(text):
    prompt = (
        "Classifique o email abaixo como 'Produtivo' ou 'Improdutivo' e sugira uma resposta automática adequada.\n"
        "Email:\n"
        f"{text}\n"
        "Responda no formato:\nCategoria: <Produtivo/Improdutivo>\nResposta: <sugestão de resposta>"
    )
    
    try:
        # Usa a API do Google AI Studio (Gemini) com modelo correto
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        output = response.text.strip()
    except Exception as e:
        return "Erro na API", f"Erro ao processar com IA: {str(e)}"
    
    categoria = "Desconhecido"
    resposta = ""
    for line in output.split('\n'):
        if line.lower().startswith("categoria:"):
            categoria = line.split(":", 1)[1].strip()
        elif line.lower().startswith("resposta:"):
            resposta = line.split(":", 1)[1].strip()
    return categoria, resposta

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/classify', methods=['POST'])
def classify():
    email_text = ""
    if 'email_file' in request.files and request.files['email_file'].filename:
        try:
            email_text = extract_text(request.files['email_file'])
        except Exception as e:
            return jsonify({'error': f"Erro ao processar arquivo: {e}"})
    elif 'email_text' in request.form and request.form['email_text'].strip():
        email_text = request.form['email_text']
    else:
        return jsonify({'error': "Nenhum email fornecido."})

    try:
        processed = preprocess_text(email_text)
    except Exception as e:
        return jsonify({'error': f"Erro ao processar texto: {e}"})

    try:
        categoria, resposta = classify_and_respond(processed)
    except Exception as e:
        return jsonify({'error': f"Erro ao consultar IA: {e}"})

    return jsonify({
        'categoria': categoria,
        'resposta': resposta,
        'email': email_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)