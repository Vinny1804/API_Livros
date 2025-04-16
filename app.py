import sqlite3

from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Same Origin Policy -> Regra entre os navegadores (Consumir uma API se estiver ambos os sites no mesmo dominio)

# CORS - Cross Origin Resource Sharing (Compartilhamento de Recursos entre origens diferentes)

# CORS desabilita o Same Origin Policy para poder consumir uma API


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

        quantidade = conn.execute("SELECT COUNT(*) FROM livros").fetchone()[0]

        if quantidade == 0:
            livros_padrao = [
            ("Harry Potter e a Pedra Fisolofal", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/81ibfYk4qmL._SY425_.jpg"),
            ("Harry Potter e a Câmara Secreta", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/51SnGLrrJcL._SY445_SX342_.jpg"),
            ("Harry Potter e o Prisioneiro de Azkaban", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/81u+ljPVifL._SY425_.jpg"),
            ("Harry Potter e o Cálice de Fogo", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/81nTLN-kz7L._SY425_.jpg"),
            ("Harry Potter e a Ordem da Fênix", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/41SknlxiqHL._SY445_SX342_.jpg"),
            ("Harry Potter e o Enigma do Príncipe", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/51msVf94L2L._SY445_SX342_.jpg"),
            ("Harry Potter e as Relíquias da Morte", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/51PoQ61oq-L._SY445_SX342_.jpg"),
            ("Diário de uma Paixão", "Romance", "Nicholas Sparks", "https://books.google.com.br/books/publisher/content?id=yRsADgAAQBAJ&hl=pt-BR&pg=PA49&img=1&zoom=3&bul=1&sig=ACfU3U1I8EkMtQJWMgWPMRCSJIHXaDmDpw&w=1280"),
            ("O Desejo", "Romance", "Nicholas Sparks", "https://books.google.com.br/books/publisher/content?id=vVA_EAAAQBAJ&hl=pt-BR&pg=PP1&img=1&zoom=3&bul=1&sig=ACfU3U3x-kTAh2duour20DIDxbvut77Fpw&w=1280"),
            ("O Diário de Anne Frank", "Biografia", "Anne Frank", "https://http2.mlstatic.com/D_NQ_NP_2X_904077-MLU50455061292_062022-F.webp"),
            ("Amigos, Amores e Aquela Coisa Terrível", "Biografia", "Matthew Perry", "https://m.media-amazon.com/images/I/41zeFYXE1aL._SY445_SX342_.jpg"),
            ("O Pequeno Príncipe", "Fábula", "Antoine de Saint-Exupéry", "https://m.media-amazon.com/images/I/81TmOZIXvzL._SL1500_.jpg"),
            ]

            for livro in livros_padrao:
                titulo, categoria, autor, image_url = livro

                conn.execute(f'''
                        INSERT INTO livros (titulo, categoria, autor, image_url)
                        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
                ''')
            conn.commit()
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
