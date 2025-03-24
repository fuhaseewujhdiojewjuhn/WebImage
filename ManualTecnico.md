# Manual Técnico - Editor de Imagens Web

## Introdução
Este documento fornece uma visão detalhada sobre a estrutura e funcionamento do Editor de Imagens Web, incluindo a arquitetura do sistema, funcionalidades e explicação do código.

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

### Arquivos e Funções

#### 1. `app.py`
Ficheiro principal da aplicação Flask, responsável pelo backend do sistema.

**Principais funcionalidades:**
- Configuração do servidor Flask
- Upload de imagens
- Aplicação de operações de edição utilizando a biblioteca Pillow
- Retorno da imagem editada via JSON

**Principais funções:**
- `process_image(image_path, operation, *args)`: Processa a imagem aplicando a operação solicitada (redimensionamento, rotação, brilho, contraste ou adição de texto).
- `upload_image()`: Gere o upload da imagem, salvando-a no diretório correto e redirecionando para a tela de edição.
- `edit_image()`: Aplica a edição na imagem carregada, salvando a versão editada e retornando-a para exibição no frontend.

#### 2. `index.html`
Página principal da aplicação, onde o utilizador pode selecionar uma imagem para upload.

**Principais componentes:**
- Formulário de upload (`<form action="/upload" method="POST" enctype="multipart/form-data">`);
- Campo de seleção do ficheiro (`<input type="file" name="file" id="file">`).

#### 3. `editor.html`
Página onde o utilizador pode visualizar a imagem original e editada, além de aplicar modificações.

**Principais componentes:**
- Seção de exibição da imagem original e editada;
- Formulário de seleção de operação;
- JavaScript para envio de requisições de edição via AJAX.

#### 4. `editor.css`
Ficheiro CSS que define o estilo da aplicação, incluindo:
- Layout responsivo;
- Estilização de botões e formulários;
- Background e aparência geral.

## Funcionamento do Sistema
### 1. Upload de Imagem
- O utilizador escolhe um ficheiro na página inicial (`index.html`);
- O formulário envia a imagem para `/upload`;
- A imagem é salva no diretório `static/uploads/`;
- O utilizador é redirecionado para a página de edição (`editor.html`).

### 2. Edição de Imagem
- O utilizador seleciona uma operação (redimensionar, rotacionar, etc.);
- O JavaScript captura os dados e envia-os via AJAX para `/edit`;
- O Flask processa a imagem e retorna o novo ficheiro;
- A imagem editada é exibida na página.

### 3. Processamento no Backend
- O Flask recebe a requisição e processa a imagem usando Pillow;
- A operação é aplicada com base nos argumentos recebidos;
- A imagem editada é salva e enviada para o frontend.

## Considerações Finais
Este manual técnico cobre os principais aspectos do Editor de Imagens Web, permitindo futuras manutenções e melhorias no projeto.

