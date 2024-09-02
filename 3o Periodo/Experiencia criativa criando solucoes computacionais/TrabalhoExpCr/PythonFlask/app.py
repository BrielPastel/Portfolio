from controllers.app_controller import create_app
from utils.create_db import create_db, db
from models import Device, Sensor, Read, Actuator, Write, User, Role
from datetime import datetime, timedelta
import random

def random_date(start, end):
    """Gera uma data aleatória entre start e end."""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

def insert_data():
    # Inserir dispositivos
    device1 = Device(name='Device1', is_active=True)
    device2 = Device(name='Device2', is_active=True)
    device3 = Device(name='Device3', is_active=True)
    device4 = Device(name='Device4', is_active=True)
    device5 = Device(name='Device5', is_active=True)
    device6 = Device(name='Device6', is_active=True)

    db.session.add(device1)
    db.session.add(device2)
    db.session.add(device3)
    db.session.add(device4)
    db.session.add(device5)
    db.session.add(device6)
    db.session.commit()

    # Inserir sensores
    sensor1 = Sensor(devices_id=device1.id, unit='Movimento', topic='botao_enviar')
    sensor2 = Sensor(devices_id=device2.id, unit='Lux', topic='light')
    sensor3 = Sensor(devices_id=device3.id, unit='Percent', topic='humidity')

    db.session.add(sensor1)
    db.session.add(sensor2)
    db.session.add(sensor3)
    db.session.commit()

    # Inserir atuadores
    actuator1 = Actuator(devices_id=device4.id, unit='On/Off', topic='botao_receber')
    actuator2 = Actuator(devices_id=device5.id, unit='Percentage', topic='dimmer')
    actuator3 = Actuator(devices_id=device6.id, unit='On/Off', topic='switch')

    db.session.add(actuator1)
    db.session.add(actuator2)
    db.session.add(actuator3)
    db.session.commit()

    # Read

    read1 = Read(sensors_id = sensor1.id, read_datetime = datetime.now() - timedelta(days=1))
    read2 = Read(sensors_id = sensor1.id, read_datetime = datetime.now())

    db.session.add(read1)
    db.session.add(read2)

    # Write

    write1 = Write(actuators_id = actuator1.id, write_datetime = datetime.now() - timedelta(days=1), value = 1)
    write2 = Write(actuators_id = actuator1.id, write_datetime = datetime.now(), value = 1)

    db.session.add(write1)
    db.session.add(write2)

    # Inserir role

    role1 = Role(role = 'common')
    role2 = Role(role = 'admin')
    role3 = Role(role = 'statistical')
    role4 = Role(role = 'operator')

    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.add(role4)
    db.session.commit()

    # Inserir usuários

    user1 = User(username='cz', password='123', user_role = 'admin')
    user2 = User(username='vitao', password='123', user_role = 'common')
    user3 = User(username='lucao', password='123', user_role = 'statistical')
    user4 = User(username='pangas', password='123', user_role = 'operator')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.commit()

    print("Dados de exemplo inseridos com sucesso.")

#criar db no MySQL
# CREATE DATABASE ra3;
# CREATE USER test1 IDENTIFIED BY "test1";
# GRANT ALL ON *.* TO test1 WITH GRANT OPTION;

if __name__ == "__main__":
    app = create_app()
    create_db(app)

    with app.app_context():
        insert_data()

    app.run(host='0.0.0.0', port=8080, debug=False)
