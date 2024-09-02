from flask import Blueprint, request, render_template

actuatorsbp = Blueprint("actuators",__name__, template_folder="templates")

actuators = ['Servo Motor', 'Lâmpada']

@actuatorsbp.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuatorsbp.route('/add_actuator', methods=['GET','POST'])
def add_actuators():
    global users
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.append(actuator)
    return render_template("list_actuators.html", devices=actuators)

@actuatorsbp.route('/list_actuators')
def list_actuators():
    return render_template("list_actuators.html", devices=actuators)

@actuatorsbp.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", devices=actuators)

@actuatorsbp.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.remove(f"{actuator}")
    return render_template("list_actuators.html", devices=actuators)
