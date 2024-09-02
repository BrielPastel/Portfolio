from flask import Flask, render_template, request
from login import login
from sensors import sensorsbp
from actuators import actuatorsbp

app = Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensorsbp, url_prefix='/')
app.register_blueprint(actuatorsbp, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
