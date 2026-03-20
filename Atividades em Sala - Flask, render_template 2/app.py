from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cadastro():
    return render_template('cadastrohtml.html')

@app.route("/login")
def login():
    return render_template('loginhtml.html')

@app.route("/homepage")
def homepage():
    return render_template('homepagehtml.html')

@app.route("/api")
def api():
    return render_template('pokemonhtml.html')

if __name__ == '__main__':
    app.run(debug=True)
