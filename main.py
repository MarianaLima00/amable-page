from flask import Flask, render_template  # Importando a função render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")  # Adicionando a importação do render_template

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

if __name__ == '__main__':
    app.run(debug=True)
