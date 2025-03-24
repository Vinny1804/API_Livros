# API Doação de Livros

Essa é uma API simples feita com Flask e SQLite para fins de estudo da escola Vai Na Web, ela permite cadastrar e listar livros doados.

## Como rodar o projeto

1. Faça o clone do repositório:
```bash 
git clone https://github.com/Vinny1804/API_Livros
cd API_Livros
```

2. Crie um ambiente virtual (Obrigatório):
```bash
python -m venv venv
source venv/Scripts/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
python app.py
```

> A Api está disponível em http: http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoint para cadastrar um novo livro

**Formato de envio dos dados**
```json
{
    "titulo":"A Sound of Thunder",
    "categoria":"Ficção Científica",
    "autor":"Ray Bradbury",
    "image_url":"https://exemplo.com"
}
```

**Resposta 201 (Created)**:
```json
{
    "mensagem":"Livro cadastrado com sucesso"
}
```

---

### GET /livros

Retorna todos os livros cadastrados em nossa API.

**Resposta (200)**:
```json
{
    "id":"1",
    "titulo":"A Sound of Thunder",
    "categoria":"Ficção Científica",
    "autor":"Ray Bradbury",
    "image_url":"https://exemplo.com"
}
```