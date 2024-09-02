from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from models.Iot.users import User
from flask_login import login_user, login_required, logout_user

usersbp = Blueprint("usersbp", __name__, template_folder="templates")

@usersbp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        user = User.validate_user(username, password)

        if user:
            login_user(user)
            return redirect(url_for('usersbp.home'))
        else:
            flash('Invalid username or password')
    return render_template("login.html")

@usersbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usersbp.login'))

@usersbp.route('/home')
@login_required
def home():
    return render_template('home.html')

@usersbp.route('/list_users')
@login_required
def list_users():
    users = User.get_username()
    return render_template("list_users.html", users = users)

@usersbp.route('/register_user')
@login_required
def register_user():
    return render_template("register_user.html")

@usersbp.route('/add_user', methods=['POST'])
@login_required
def add_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        role = request.form['role']
        User.save_user(user, password, role)
    return redirect(url_for('usersbp.list_users'))

@usersbp.route('/edit_user')
@login_required
def edit_user():
    id = request.args.get('id', None)
    user = User.get_single_user(id)
    return render_template("update_user.html", user = user)

@usersbp.route('/update_user', methods=['POST'])
@login_required
def update_user():
    id = request.form.get("id")
    user = request.form.get("user")
    password = request.form.get("password")
    role = request.form.get("role")
    User.update_user(id, user, password, role)

    return redirect(url_for('usersbp.list_users'))

@usersbp.route('/del_user', methods=['GET'])
@login_required
def del_user():
    id = request.args.get('id', None)
    User.delete_user(id)
    return redirect(url_for('usersbp.list_users'))
