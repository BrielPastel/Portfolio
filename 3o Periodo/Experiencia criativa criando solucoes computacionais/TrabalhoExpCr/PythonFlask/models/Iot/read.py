from models.db import db
from models.Iot.sensors import Sensor
from models.Iot.devices import Device
from datetime import datetime
from sqlalchemy import desc

class Read(db.Model):
    __tablename__ = 'read'
    id= db.Column('id', db.Integer, nullable = False, primary_key=True)
    read_datetime = db.Column(db.DateTime(), nullable = False)
    sensors_id= db.Column(db.Integer, db.ForeignKey(Sensor.id), nullable = False)
    
    def save_read(topic):
        sensor = Sensor.query.filter(Sensor.topic == topic).first()
        device = Device.query.filter(Device.id == sensor.devices_id).first()
        if (sensor is not None) and (device.is_active==True):
            read = Read( read_datetime = datetime.now(), sensors_id = sensor.id)
            db.session.add(read)
            db.session.commit()
    
    def get_read(device_id, start, end):
        sensor = Sensor.query.filter(Sensor.devices_id == device_id).first()
        read = Read.query.filter(Read.sensors_id == sensor.id,
                                 Read.read_datetime > start,
                                 Read.read_datetime<end).all()
        return read
    
    def get_last_read_datetime():
        last_read = Read.query.order_by(desc(Read.read_datetime)).first()
        return last_read.read_datetime if last_read else None