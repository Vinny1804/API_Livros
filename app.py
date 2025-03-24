from flask import Flask,request,jsonify

import sqlite3

app = Flask(__name__)

# route --> São os endpoint da nossa API
@app.route('/')
def home():
    return "<h2>Seja o motivo de alguém sorrir hoje, mesmo que esse alguém seja você.</h2>"

def init_db():
    # Crie o nosso banco de dados com um arquivo'database.db' e conecte a variável conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    image_url TEXT NOT NULL
                )
            """
        )
init_db()


@app.route("/doar", methods=["POST"])
def doar():
    # Variável dados receba a resposta do cliente em JSON
    dados = request.get_json()
    print(f'AQUI ESTÃO OS DADOS RETORNADOS DO CLIENTE {dados}')

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400 # 400 Indica que o servidor não pode processar uma solicitação

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url)
            VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)

    conn.commit() # Comando para salvar as informações no banco de dados

    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall() # fetchall() - 'Traduzir' para o formato que o python entenda (SQL -> Python)

        livros_formatados = [] 

        for item in livros:
            # O item vai passar por cada informação no banco de dados e estruturar elas
            dicionario_livros = {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4]
            }
            livros_formatados.append(dicionario_livros) # append() adiciona uma informação no final da lista

    return jsonify(livros_formatados)



# Se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)
