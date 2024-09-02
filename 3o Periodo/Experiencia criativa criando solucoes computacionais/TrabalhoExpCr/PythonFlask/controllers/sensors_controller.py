from flask import Blueprint, request, render_template
from flask import redirect, url_for
from models.Iot.sensors import Sensor
from flask_login import login_required

sensorsbp = Blueprint("sensors",__name__, template_folder="templates")

@sensorsbp.route('/list_sensors')
@login_required
def list_sensors():
    sensors = Sensor.get_sensors()
    return render_template("list_sensors.html", sensors = sensors)

@sensorsbp.route('/register_sensor')
@login_required
def register_sensor():
    return render_template("register_sensor.html")

@sensorsbp.route('/add_sensor', methods=['GET','POST'])
@login_required
def add_sensor():
    name = request.form.get("name")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, topic, unit, is_active)

    return redirect(url_for('sensors.list_sensors'))

@sensorsbp.route('/edit_sensor')
@login_required
def edit_sensor():
    id = request.args.get('id', None)
    sensors = Sensor.get_single_sensor(id)
    return render_template("update_sensor.html", sensor = sensors)

@sensorsbp.route('/update_sensor', methods=['POST'])
@login_required
def update_sensor():
    id = request.form.get("id")
    name = request.form.get("name")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False
    Sensor.update_sensor(id, name, topic, unit, is_active)

    return redirect(url_for('sensors.list_sensors'))

@sensorsbp.route('/del_sensor', methods=['GET'])
@login_required
def del_sensor():
    id = request.args.get('id', None)
    Sensor.delete_sensor(id)
    return redirect(url_for('sensors.list_sensors'))
