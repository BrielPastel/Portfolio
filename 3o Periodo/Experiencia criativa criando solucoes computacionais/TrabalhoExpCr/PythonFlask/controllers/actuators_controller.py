from flask import Blueprint, request, render_template
from flask import redirect, url_for
from models.Iot.actuators import Actuator
from flask_login import login_required

actuatorsbp = Blueprint("actuators",__name__, template_folder="templates")

@actuatorsbp.route('/list_actuators')
@login_required
def list_actuators():
    actuators = Actuator.get_actuators()
    return render_template("list_actuators.html", actuators = actuators)

@actuatorsbp.route('/register_actuator')
@login_required
def register_actuator():
    return render_template("register_actuator.html")

@actuatorsbp.route('/add_actuator', methods=['GET','POST'])
@login_required
def add_actuator():
    name = request.form.get("name")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator.save_actuator(name, topic, unit, is_active)

    return redirect(url_for('actuators.list_actuators'))

@actuatorsbp.route('/edit_actuator')
@login_required
def edit_actuator():
    id = request.args.get('id', None)
    actuators = Actuator.get_single_actuator(id)
    return render_template("update_actuator.html", actuator = actuators)

@actuatorsbp.route('/update_actuator', methods=['POST'])
@login_required
def update_actuator():
    id = request.form.get("id")
    name = request.form.get("name")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False
    Actuator.update_actuator(id, name, topic, unit, is_active)

    return redirect(url_for('actuators.list_actuators'))

@actuatorsbp.route('/del_actuator', methods=['GET'])
@login_required
def del_actuator():
    id = request.args.get('id', None)
    Actuator.delete_actuator(id)
    return redirect(url_for('actuators.list_actuators'))
