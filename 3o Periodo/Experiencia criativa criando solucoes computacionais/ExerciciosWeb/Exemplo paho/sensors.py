from flask import Blueprint, request, render_template

sensorsbp = Blueprint("sensors",__name__, template_folder="templates")

sensors = ['Umidade', 'Temperatura', 'Luminosidade']

@sensorsbp.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensorsbp.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor')
    sensors.append(sensor)
    return render_template("list_sensors.html", devices=sensors)

@sensorsbp.route('/list_sensors')
def list_sensors():
    return render_template("list_sensors.html", devices=sensors)

@sensorsbp.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", devices=sensors)

@sensorsbp.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor')
    sensors.remove(f"{sensor}")
    return render_template("list_sensors.html", devices=sensors)