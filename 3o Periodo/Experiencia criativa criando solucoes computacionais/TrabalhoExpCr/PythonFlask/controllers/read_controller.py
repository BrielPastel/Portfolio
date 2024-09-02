from flask import Blueprint, request, render_template
from models.Iot.read import Read
from models.Iot.sensors import Sensor
from flask_login import login_required

readsbp = Blueprint("read",__name__, template_folder="views")

@readsbp.route("/history_read")
@login_required
def history_read():
    sensors = Sensor.get_sensors()
    read = {}
    return render_template("history_read.html", sensors = sensors, read = read)

@readsbp.route("/get_read", methods=['POST'])
@login_required
def get_read():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        read = Read.get_read(id, start, end)
        sensors = Sensor.get_sensors()
        return render_template("history_read.html", sensors = sensors, read = read)
    
@readsbp.route('/tempo_real')
@login_required
def tempo_real():
    last_read_datetime = Read.get_last_read_datetime()
    if last_read_datetime:
        dia = last_read_datetime.day
        mes = last_read_datetime.month
        ano = last_read_datetime.year
        hora = last_read_datetime.hour
        minuto = last_read_datetime.minute
        segundo = last_read_datetime.second
        values = {
            'dia': dia, 'mes': mes, 'ano': ano,
            'hora': hora, 'minuto': minuto, 'segundo': segundo
        }
    else:
        values = {
            'dia': 0, 'mes': 0, 'ano': 0,
            'hora': 0, 'minuto': 0, 'segundo': 0
        }
    return render_template("tempo_real.html", values=values)