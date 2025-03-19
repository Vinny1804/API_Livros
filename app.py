from flask import Flask,request,jsonify

import sqlite3

app = Flask(__name__)

# route --> São os endpoint da nossa API

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

# Se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)
