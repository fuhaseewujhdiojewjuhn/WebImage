# Editor de Imagens Web

## Descrição
Este é um editor de imagens web desenvolvido com Python, Flask, HTML, CSS e JavaScript. Ele permite o upload de imagens e a aplicação de edições como redimensionamento, rotação, ajuste de brilho, contraste e adição de texto.

## Funcionalidades
- Upload de imagens
- Redimensionamento de imagens
- Rotação de imagens
- Ajuste de brilho e contraste
- Adição de texto sobre a imagem
- Visualização da imagem original e editada

## Tecnologias Utilizadas
- Python (Flask)
- HTML, CSS e JavaScript
- Biblioteca Pillow para manipulação de imagens

## Estrutura do Projeto
```
/ Editor de Imagens Web
|-- static/
|   |-- css/
|   |   |-- editor.css
|   |-- uploads/
|-- templates/
|   |-- index.html
|   |-- editor.html
|-- app.py
|-- README.md
```

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio/editor-imagens-web.git
   cd editor-imagens-web
   ```
2. Instale as dependências:
   ```bash
   pip install flask pillow
   ```
3. Execute a aplicação:
   ```bash
   python app.py
   ```
4. Acesse no navegador:
   ```
   http://127.0.0.1:5000/
   ```

## Uso
- Acesse a página inicial e carregue uma imagem.
- Escolha uma operação (redimensionar, rotacionar, brilho, contraste, texto) e forneça os parâmetros necessários.
- Aplique a edição e visualize a imagem modificada.

## Autor
Desenvolvido por Beatriz Gomes, Brena Picado e Salvador Raposo

