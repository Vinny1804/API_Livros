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
                    imagem_url TEXT NOT NULL
                )
            """
        )
init_db()

app.route("/doar", methods=["POST"])
def doar():
    # Variável dados receba a resposta do cliente em JSON
    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400 # 400 Indica que o servidor não pode processar uma solicitação





# Se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)

# # É o comando para rodar a nossa aplicação
# app.run()