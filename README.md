# 🤖 Classificador de Emails com IA

Uma aplicação web inteligente que utiliza Inteligência Artificial para classificar emails automaticamente e sugerir respostas apropriadas.

## 📋 Descrição

Esta aplicação foi desenvolvida para ajudar usuários a:
- **Classificar emails** automaticamente por categoria
- **Gerar respostas sugeridas** baseadas no conteúdo do email
- **Processar arquivos** (.txt e .pdf) ou texto direto
- **Interface moderna** e responsiva

## 🚀 Como Funcionar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd email_classifier_app_ready
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
python app.py
```

4. **Acesse no navegador:**
```
http://localhost:5000
```

## 🎯 Como Usar

### 1. Upload de Arquivo
- **Formatos aceitos**: `.txt` ou `.pdf`
- Clique no botão "Selecionar" à direita
- Escolha o arquivo que contém o email
- O nome do arquivo aparecerá na caixa de texto

### 2. Texto Direto
- Cole o texto do email diretamente na caixa de texto
- Não há limite de caracteres
- Pode ser usado como alternativa ao upload

### 3. Classificação
- Clique em "Classificar e Sugerir Resposta"
- A IA analisará o conteúdo do email
- Aguarde o processamento (indicado pela animação)

### 4. Resultados
- **Categoria**: Classificação automática do email
- **Resposta sugerida**: Sugestão de resposta baseada na IA
- **Texto analisado**: Visualize o email processado (expandível)

## 🏗️ Estrutura do Projeto

```
email_classifier_app_ready/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── static/
│   └── styles.css        # Estilos CSS da interface
└── templates/
    └── index.html        # Template HTML principal
```

## 🎨 Características da Interface

### Design Moderno
- **Fundo branco** limpo e profissional
- **Tipografia Poppins** moderna e legível
- **Animações suaves** para melhor experiência
- **Layout responsivo** para todos os dispositivos

### Elementos Visuais
- **Gradientes** em botões e títulos
- **Sombras sutis** para profundidade
- **Ícones** para melhor identificação
- **Estados hover** interativos

### Funcionalidades
- **Upload de arquivo** com botão simples
- **Área de texto** redimensionável
- **Feedback visual** durante processamento
- **Exibição de resultados** organizada

## 🔧 Tecnologias Utilizadas

### Backend
- **Flask**: Framework web Python
- **Python**: Linguagem principal
- **IA/ML**: Para classificação e geração de respostas

### Frontend
- **HTML5**: Estrutura da página
- **CSS3**: Estilização moderna
- **JavaScript**: Interações dinâmicas
- **Google Fonts**: Tipografia Poppins

### Dependências
- Flask
- Outras bibliotecas listadas em `requirements.txt`

## 📱 Responsividade

A aplicação é totalmente responsiva e funciona em:
- **Desktop**: Interface completa
- **Tablet**: Layout adaptado
- **Mobile**: Versão otimizada para toque

## 🎯 Casos de Uso

### Profissionais
- **Atendimento ao cliente**: Classificar e responder emails
- **Suporte técnico**: Organizar solicitações
- **Vendas**: Categorizar leads e oportunidades

### Pessoais
- **Organização de emails**: Classificar correspondência
- **Automação**: Respostas rápidas e consistentes
- **Produtividade**: Economizar tempo na gestão de emails

## 🔒 Segurança

- **Validação de arquivos**: Apenas formatos permitidos
- **Processamento local**: Dados não são enviados externamente
- **Interface segura**: Sem vulnerabilidades conhecidas

## 🚀 Melhorias Futuras

- [ ] Suporte a mais formatos de arquivo
- [ ] Histórico de classificações
- [ ] Personalização de categorias
- [ ] Integração com servidores de email
- [ ] API REST para integração

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

**Desenvolvido com ❤️ para facilitar a gestão de emails**
