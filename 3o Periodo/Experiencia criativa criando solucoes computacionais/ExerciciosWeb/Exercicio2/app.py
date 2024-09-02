from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h2>Minha Casa</h2>
            <h3>Acesse os cômodos:</h3>
            <ul>
                <li><a href="/quarto">Quarto</a></li>
                <li><a href="/banheiro">Banheiro</a></li>
            </ul>
        </body>
    </html>
    """

@app.route('/quarto')
def quarto():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Quarto</h1>
            <h2>Acesse o menu</h2>
            <ul>
                <li><a href="/quarto/sensores">Listar Sensores</a></li>
                <li><a href="/quarto/atuadores">Listar Atuadores</a></li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>!</p>
        </body>
    </html>
    """

@app.route('/quarto/sensores')
def sensoresQuarto():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Sensores do quarto</h1>
            <h2>Sensores</h2>
            <ul>
                <li>Sensor de luminosidade</li>
            </ul>
            <p>Voltar para <a href="/quarto">quarto</a>!</p>
        </body>
    </html>
    """

@app.route('/quarto/atuadores')
def atuadoresQuarto():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Atuadores do quarto</h1>
            <h2>Atuadores</h2>
            <ul>
                <li>Interruptor</li>
            </ul>
            <p>Voltar para <a href="/quarto">quarto</a>!</p>
        </body>
    </html>
    """

@app.route('/banheiro')
def banheiro():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Banheiro</h1>
            <h2>Acesse o menu</h2>
            <ul>
                <li><a href="/banheiro/sensores">Listar Sensores</a></li>
                <li><a href="/banheiro/atuadores">Listar Atuadores</a></li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>!</p>
        </body>
    </html>
    """

@app.route('/banheiro/sensores')
def sensoresBanheiro():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Sensores do banheiro</h1>
            <h2>Sensores</h2>
            <ul>
                <li>Sensor de umidade</li>
            </ul>
            <p>Voltar para <a href="/banheiro">banheiro</a>!</p>
        </body>
    </html>
    """

@app.route('/banheiro/atuadores')
def atuadoresBanheiro():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Atuadores do banheiro</h1>
            <h2>Atuadores</h2>
            <ul>
                <li>Lâmpada inteligente</li>
            </ul>
            <p>Voltar para <a href="/banheiro">banheiro</a>!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
