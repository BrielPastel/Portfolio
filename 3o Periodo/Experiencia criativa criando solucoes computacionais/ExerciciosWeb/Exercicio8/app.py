from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    quartos = {"Quarto":"/quarto", "Banheiro":"/banheiro"}
    return render_template("index.html", quartos=quartos)

@app.route('/quarto')
def quarto():
    itensQuarto = {"Listar Sensores":"/quarto/sensores", "Listar Atuadores":"/quarto/atuadores"}
    return render_template("quarto.html", itensQuarto=itensQuarto)

@app.route('/quarto/sensores')
def sensoresQuarto():
    dispositivos = ["Sensor de luminosidade", "Sensor de calor"]
    return render_template("sensoresQuarto.html", dispositivos=dispositivos)

@app.route('/quarto/atuadores')
def atuadoresQuarto():
    dispositivos = ["Interruptor", "Ar condicionado"]
    return render_template("atuadoresQuarto.html", dispositivos=dispositivos)

@app.route('/banheiro')
def banheiro():
    itensBanheiro = {"Listar Sensores":"/banheiro/sensores", "Listar Atuadores":"/banheiro/atuadores"}
    return render_template("banheiro.html", itensBanheiro=itensBanheiro)

@app.route('/banheiro/sensores')
def sensoresBanheiro():
    dispositivos = ["Sensor de humidade", "Sensor de bosta"]
    return render_template("sensoresBanheiro.html", dispositivos=dispositivos)

@app.route('/banheiro/atuadores')
def atuadoresBanheiro():
    dispositivos = ["Lâmpada inteligente", "Aquecedor"]
    return render_template("atuadoresBanheiro.html", dispositivos=dispositivos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
