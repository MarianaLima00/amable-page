from flask import Flask, render_template  # Importando a função render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")  # Adicionando a importação do render_template


if __name__ == '__main__':
    app.run(debug=True)
