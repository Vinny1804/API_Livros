from flask import Flask

import sqlite3

app = Flask(__name__)

# route --> São os endpoint da nossa API
@app.route("/")
def pagar_pessoas():
    return "<h1>Começar a semana, pagando suas dívidas, é bom demais</h1>"

@app.route("/pix")
def mande_o_pix():
    return "<h3>Pagar as pessoas faz bem pra pessoas!! =D</h3>"

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



# Se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)

# # É o comando para rodar a nossa aplicação
# app.run()