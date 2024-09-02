#app_controller.py
from flask import Flask, render_template, request, jsonify
from models.db import db, instance

import json
from flask_mqtt import Mqtt
from controllers.sensors_controller import sensor_
from controllers.actuators_controller import actuator_
from controllers.read_controller import read
from controllers.write_controller import write
from models.Iot.read import Read
from models.Iot.write import Write


def create_app():
    app = Flask(__name__, 
                template_folder="./views/", 
                static_folder="./static/",
                root_path="./")

    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5000  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

    mqtt_client= Mqtt()
    mqtt_client.init_app(app)

    sensor_topic = "/aula_flask/"
    actuator_topic = "/aula_flask/actuator1000"

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Broker Connected successfully')
            mqtt_client.subscribe(actuator_topic)
            mqtt_client.subscribe(sensor_topic)  #subscribe topic
        else:
             print('Bad connection. Code:', rc)
             

    #@mqtt_client.on_disconnect()
    #def handle_disconnect(client, userdata, rc):
    #    print("Disconnected from broker")


    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        if(message.topic==sensor_topic):
            js = json.loads(message.payload.decode())
            print(js)
            try:
                with app.app_context():
                    Read.save_read(js["sensor"],js["valor"])
            except:
                pass
        elif(message.topic==actuator_topic):
            valor = message.payload.decode()
            print(valor)
            try:
                with app.app_context():
                    Write.save_write(actuator_topic,valor)
            except:
                pass

        

    
    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuator_, url_prefix='/')
    app.register_blueprint(read, url_prefix='/')
    app.register_blueprint(write, url_prefix='/')
    
    

    @app.route('/')
    def index():
        return render_template("home.html")
    
    @app.route('/home')
    def home():
        return render_template("home.html")
    
    @app.route('/publish')
    def publish():
        return render_template("publish.html")
    
    @app.route('/publish_message', methods=['GET','POST'])
    def publish_message():
        request_data = request.get_json()
        publish_result = mqtt_client.publish(request_data['topic'], request_data['message'])
        return jsonify(publish_result)
    
    return app
