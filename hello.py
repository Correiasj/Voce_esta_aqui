

from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template("planeta.html")

# Rota que renderiza uma página HTML
@app.route('/pagina-html')
def pagina_html():
    return render_template('pagina.html')


# Rota com variável na URL
@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)

