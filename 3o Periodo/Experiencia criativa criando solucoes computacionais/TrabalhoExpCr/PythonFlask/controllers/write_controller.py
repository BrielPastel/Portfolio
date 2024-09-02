from flask import Blueprint, request, render_template
from models.Iot.write import Write
from models.Iot.actuators import Actuator
from flask_login import login_required

writesbp = Blueprint("write",__name__, template_folder="views")

@writesbp.route("/history_write")
@login_required
def history_write():
    actuators = Actuator.get_actuators()
    write = {}
    return render_template("history_write.html", actuators = actuators, write = write)

@writesbp.route("/get_write", methods=['POST'])
@login_required
def get_write():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        write = Write.get_write(id, start, end)
        actuators = Actuator.get_actuators()
        return render_template("history_write.html", actuators = actuators, write = write)
    