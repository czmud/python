from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/users/')
def index():
    users = User.get_all()
    return render_template("index.html", users = users)
@app.route('/users/new/')
def user_form():
    return render_template("create_user.html")
@app.route('/create_user/', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')