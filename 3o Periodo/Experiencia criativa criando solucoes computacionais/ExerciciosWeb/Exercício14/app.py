from flask import Flask, render_template, request

app= Flask(__name__)

users = {
'vitao': 'vitaosenha',
'vitao2': 'vitaosenha'
}
sensors = ['Umidade', 'Temperatura', 'Luminosidade']
actuators = ['Servo Motor', 'Lâmpada']

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
    
@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("list_users.html", devices=users)

@app.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.append(sensor)
    return render_template("list_sensors.html", devices=sensors)

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuators():
    global users
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.append(actuator)
    return render_template("list_actuators.html", devices=actuators)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)

@app.route('/list_sensors')
def list_sensors():
    return render_template("list_sensors.html", devices=sensors)

@app.route('/list_actuators')
def list_actuators():
    return render_template("list_actuators.html", devices=actuators)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
