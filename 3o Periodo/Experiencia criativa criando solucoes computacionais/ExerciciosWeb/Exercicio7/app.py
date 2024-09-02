# app.py
from flask import Flask, render_template

app= Flask(__name__)

## __name__ is the application name
@app.route('/')
def index():
    rooms = {"Bedroom":"/bedroom",}
    return render_template("index.html")

@app.route('/sensores')
def sensores():
    sensores = {'Umidade':4, 'Temperatura':12, 'Luminosidade':25}
    return render_template("sensores.html", sensores=sensores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
