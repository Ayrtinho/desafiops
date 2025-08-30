# 🤖 Classificador de Emails com IA

Uma aplicação web inteligente que utiliza Inteligência Artificial (Google Gemini) para classificar emails automaticamente e sugerir respostas apropriadas.

## 📋 Descrição

Esta aplicação foi desenvolvida para ajudar usuários a:
- **Classificar emails** automaticamente como "Produtivo" ou "Improdutivo"
- **Gerar respostas sugeridas** baseadas no conteúdo do email usando IA
- **Processar arquivos** (.txt e .pdf) ou texto direto
- **Interface moderna** e responsiva com design atualizado

## 🚀 Como Funcionar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Chave de API do Google AI Studio (Gemini)

### Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd desafio
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure a API Key (opcional):**
   - Edite o arquivo `app.py`
   - Substitua a chave da API na linha 12:
   ```python
   GOOGLE_API_KEY = "sua-chave-api-aqui"
   ```

4. **Execute a aplicação:**
```bash
python app.py
```

5. **Acesse no navegador:**
```
http://localhost:8080
```

## 🎯 Como Usar

### 1. Upload de Arquivo
- **Formatos aceitos**: `.txt` ou `.pdf`
- Clique no botão "Selecionar" à direita
- Escolha o arquivo que contém o email
- O nome do arquivo e tamanho aparecerão na interface

### 2. Texto Direto
- Cole o texto do email diretamente na caixa de texto
- Não há limite de caracteres
- Pode ser usado como alternativa ao upload

### 3. Classificação
- Clique em "Classificar e Sugerir Resposta"
- A IA (Google Gemini) analisará o conteúdo do email
- Aguarde o processamento (indicado pela animação de loading)

### 4. Resultados
- **Categoria**: Classificação automática (Produtivo/Improdutivo)
- **Resposta sugerida**: Sugestão de resposta baseada na IA
- **Texto analisado**: Visualize o email processado (expandível)

## 🏗️ Estrutura do Projeto

```
desafio/
├── app.py                 # Aplicação principal Flask
├── index.html             # Interface HTML (na raiz)
├── styles.css             # Estilos CSS (na raiz)
├── requirements.txt       # Dependências Python
└── README.md             # Este arquivo
```

## 🎨 Características da Interface

### Design Moderno
- **Fundo branco** limpo e profissional
- **Tipografia Poppins e Inter** moderna e legível
- **Animações suaves** para melhor experiência
- **Layout responsivo** para todos os dispositivos
- **Gradientes** em botões e títulos
- **Sombras sutis** para profundidade

### Elementos Visuais
- **Ícones** para melhor identificação
- **Estados hover** interativos
- **Upload de arquivo** com feedback visual
- **Área de texto** redimensionável
- **Loading animado** durante processamento
- **Resultados organizados** com expansão de detalhes

## 🔧 Tecnologias Utilizadas

### Backend
- **Flask**: Framework web Python
- **Google Generative AI**: API do Gemini para IA
- **NLTK**: Processamento de linguagem natural
- **PyPDF2**: Leitura de arquivos PDF

### Frontend
- **HTML5**: Estrutura da página
- **CSS3**: Estilização moderna com animações
- **JavaScript**: Interações dinâmicas e AJAX
- **Google Fonts**: Tipografia Poppins e Inter

### Dependências Principais
```
flask
flask-cors
google-generativeai
PyPDF2
nltk
```

## 🤖 Inteligência Artificial

### Google Gemini
- **Modelo**: gemini-1.5-flash
- **Função**: Classificação e geração de respostas
- **Processamento**: Análise de texto em português
- **Saída**: Categoria + resposta sugerida

### Processamento de Texto
- **NLTK**: Tokenização e remoção de stopwords
- **RSLPStemmer**: Stemming específico para português
- **Pré-processamento**: Limpeza e normalização do texto

## 📱 Responsividade

A aplicação é totalmente responsiva e funciona em:
- **Desktop**: Interface completa com todas as funcionalidades
- **Tablet**: Layout adaptado para telas médias
- **Mobile**: Versão otimizada para toque e telas pequenas

## 🎯 Casos de Uso

### Profissionais
- **Atendimento ao cliente**: Classificar e responder emails automaticamente
- **Suporte técnico**: Organizar solicitações por prioridade
- **Vendas**: Categorizar leads e oportunidades
- **RH**: Triagem de candidaturas e solicitações

### Pessoais
- **Organização de emails**: Classificar correspondência pessoal
- **Automação**: Respostas rápidas e consistentes
- **Produtividade**: Economizar tempo na gestão de emails

## 🔒 Segurança e Privacidade

- **Validação de arquivos**: Apenas formatos permitidos (.txt, .pdf)
- **Processamento via API**: Dados enviados para Google AI Studio
- **Interface segura**: Validação de entrada e saída
- **Sem armazenamento**: Dados não são salvos localmente

## 🚀 Melhorias Futuras

- [ ] Suporte a mais formatos de arquivo (.docx, .eml)
- [ ] Histórico de classificações
- [ ] Personalização de categorias
- [ ] Integração com servidores de email
- [ ] API REST para integração externa
- [ ] Cache de resultados para melhor performance
- [ ] Suporte a múltiplos idiomas

## 🐛 Solução de Problemas

### Problemas Comuns

1. **CSS não carrega:**
   - Verifique se o servidor está rodando na porta 8080
   - Recarregue a página (Ctrl+F5)

2. **IA não responde:**
   - Verifique a conexão com a internet
   - Confirme se a API key está configurada
   - Verifique os logs do servidor

3. **Arquivo não é processado:**
   - Confirme se o formato é .txt ou .pdf
   - Verifique se o arquivo não está corrompido

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Entre em contato com a equipe de desenvolvimento

---

**Desenvolvido com ❤️ para facilitar a gestão de emails usando IA**
