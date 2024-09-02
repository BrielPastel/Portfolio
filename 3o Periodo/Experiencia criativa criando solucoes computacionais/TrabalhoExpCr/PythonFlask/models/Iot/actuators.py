from models.db import db
from models.Iot.devices import Device

class Actuator(db.Model):
    __tablename__ = 'actuators'
    id= db.Column('id', db.Integer, primary_key=True)
    devices_id = db.Column( db.Integer, db.ForeignKey(Device.id))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))
    writes = db.relationship("Write", cascade="all, delete", backref="actuator")

    def get_actuators():
        query = Actuator.query.join(Device, Device.id == Actuator.devices_id)\
                        .add_columns(Device.id, Device.name,
                                Device.is_active, Actuator.topic,
                                Actuator.unit)
        actuators = query.all()
        return actuators
    
    def save_actuator(name, topic, unit, is_active):
        device = Device(name = name, is_active = is_active)
        actuator = Actuator(devices_id = device.id, unit= unit, topic = topic)

        device.actuators.append(actuator)
        db.session.add(device)
        db.session.commit()

    def get_single_actuator(id):
        actuator = Actuator.query.filter(Actuator.devices_id == id).first()
        if actuator is not None:
            actuator = Actuator.query.filter(Actuator.devices_id == id)\
            .join(Device).add_columns(Device.id, Device.name, Device.is_active, Actuator.topic, Actuator.unit).first()
        return [actuator]
    
    def update_actuator(id, name, topic, unit, is_active):
        device = Device.query.filter(Device.id == id).first()
        actuator = Actuator.query.filter(Actuator.devices_id == id).first()
        if device is not None:
            device.name = name
            actuator.topic = topic
            actuator.unit = unit
            device.is_active = is_active
            db.session.commit()
        
    def delete_actuator(id):
        print(id)
        device = db.session.query(Device).get(id)
        print(device)
        db.session.delete(device)
        db.session.commit()
        
        return Actuator.get_actuators()