from flask import Flask, render_template, request, jsonify, redirect, url_for
from models.db import db, instance
from flask_mqtt import Mqtt
from controllers.users_controller import usersbp
from controllers.sensors_controller import sensorsbp
from controllers.actuators_controller import actuatorsbp
from controllers.read_controller import readsbp
from controllers.write_controller import writesbp
from models.Iot.users import User
from models.Iot.read import Read
from models.Iot.write import Write
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import json


def create_app():
    app = Flask(__name__,
                template_folder="./views/",
                static_folder="./static/",
                root_path="./")

    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'usersbp.login'  # A rota de login no seu Blueprint

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  
    app.config['MQTT_PASSWORD'] = ''  
    app.config['MQTT_KEEPALIVE'] = 5000  
    app.config['MQTT_TLS_ENABLED'] = False 

    mqtt_client= Mqtt()
    mqtt_client.init_app(app)
    mqtt = Mqtt(app)

    sensor_topic = "botao_enviar"
    actuator_topic = "botao_receber"

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Broker Connected successfully')
            mqtt_client.subscribe(sensor_topic)
            mqtt_client.subscribe(actuator_topic)
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        global ano, mes, dia, semana, hora, minuto, segundo
        if(message.topic==sensor_topic):
            js = json.loads(message.payload.decode())
            try:
                with app.app_context():
                    print(f"Read: {js}")
                    if js['movimento']:
                        print("Funcionou")
                        Read.save_read(sensor_topic)
            except:
                pass
        elif(message.topic==actuator_topic):
            valor = message.payload.decode()
            try:
                with app.app_context():
                    print(f"Write: {valor[13]}")
                    Write.save_write(actuator_topic,valor[13])
            except:
                pass


    app.register_blueprint(usersbp, url_prefix='/')
    app.register_blueprint(sensorsbp, url_prefix='/')
    app.register_blueprint(actuatorsbp, url_prefix='/')
    app.register_blueprint(readsbp, url_prefix='/')
    app.register_blueprint(writesbp, url_prefix='/')


    @app.route('/')
    def index():
        return redirect(url_for('usersbp.login'))
    
    @app.route('/publish')
    @login_required
    def publish():
        return render_template('publish.html')
    
    @app.route('/publish_message', methods=['POST'])
    @login_required
    def publish_message():
        request_data = request.get_json()
        mqtt_client.publish("botao_receber", json.dumps(request_data))
        return jsonify({"success": True})
    
    return app