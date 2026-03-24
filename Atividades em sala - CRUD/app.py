from flask import Flask
import sqlite3, os

conn = sqlite3.connect('meu_banco.db') #conecta como o banco de dados (cria o arquivo se não tiver)
conn.close()

app = Flask(__name__)

@app.route('/')
def home():
    return "Texto", 200

if __name__ == "__main__":
    app.run(debug=True)