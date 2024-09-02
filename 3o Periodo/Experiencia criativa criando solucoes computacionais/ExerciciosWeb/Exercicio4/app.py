from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quarto')
def quarto():
    return render_template("quarto.html")

@app.route('/quarto/sensores')
def sensoresQuarto():
    return render_template("sensoresQuarto.html")

@app.route('/quarto/atuadores')
def atuadoresQuarto():
    return render_template("atuadoresQuarto.html")

@app.route('/banheiro')
def banheiro():
    return render_template("banheiro.html")

@app.route('/banheiro/sensores')
def sensoresBanheiro():
    return render_template("sensoresBanheiro.html")

@app.route('/banheiro/atuadores')
def atuadoresBanheiro():
    return render_template("atuadoresBanheiro.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
