from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user
from UserLogin import UserLogin
from main import app
from admin_auth import get_user, finalize, check_user, get_user_by_username, add_user, set_permission_level, remove_user


login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        user = UserLogin().fromDB(user_id, get_user)
    except:
        user = None
    return user

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if check_user(username, password):
            user = get_user_by_username(username)
            userLogin = UserLogin().create(user)
            login_user(userLogin)
            return redirect(url_for("main"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = add_user(username, password)
        print(user)
        if user:
            userLogin = UserLogin().create(user)
            login_user(userLogin)
            return redirect(url_for("main"))
    return render_template("register.html")