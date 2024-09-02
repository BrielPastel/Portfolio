from flask import Flask, render_template, request

app= Flask(__name__)

users = {
'vitao': 'vitaosenha',
'vitao2': 'vitaosenha'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>Você não é o vitao!</h1>'
    else:
        return render_template('login.html')

@app.route('/sensores')
def sensores():
    sensores = ['Umidade', 'Temperatura', 'Luminosidade']
    return render_template("sensores.html", sensores=sensores)

@app.route('/atuadores')
def atuadores():
    atuadores = {'Servo Motor':0, 'Lâmpada':1}
    return render_template("atuadores.html", atuadores=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
