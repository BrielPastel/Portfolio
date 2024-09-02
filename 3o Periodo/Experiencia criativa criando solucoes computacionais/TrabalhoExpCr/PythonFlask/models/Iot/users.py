from models.db import db
from flask_login import UserMixin
from models.Iot.roles import Role

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    user_role = db.Column(db.String(50), db.ForeignKey(Role.role), nullable = False)

    def get_username():
        query = User.query.with_entities(User.id, User.username, User.password, User.user_role)
        users = query.all()
        return users

    def validate_user(username, password):
        return User.query.filter_by(username=username, password=password).first()
    
    def save_user(username, password, role):
        user = User(username = username, password = password, role = role)

        db.session.add(user)
        db.session.commit()

    def get_single_user(id):
        user = User.query.filter_by(id=id).first()
        if user is not None:
            user = User.query.with_entities(User.id, User.username, User.password, User.user_role).filter_by(id=id).first()
        return [user]
    
    def update_user(id, username, password, role):
        user = User.query.filter_by(id=id).first()
        if user is not None:
            user.username = username
            user.password = password
            user.user_role = role
            db.session.commit()
            return True
        return False
    
    def delete_user(id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False