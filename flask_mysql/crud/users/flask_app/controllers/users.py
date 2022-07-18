from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
@app.route('/users/')
def index():
    users = User.get_all()
    return render_template("index.html", users = users)
@app.route('/users/new/')
def user_form():
    return render_template("createuser.html")
@app.route('/users/<int:user_id>/')
def display_user(user_id):
    print(user_id)
    data = { "id": user_id }
    user = User.get_user_by_id(data)
    return render_template("displayuser.html", user = user)
@app.route('/create_user/', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')
@app.route('/users/<int:user_id>/edit/')
def display_user_edit(user_id):
    data = { "id": user_id }
    user = User.get_user_by_id(data)
    return render_template("edituser.html", user=user)
@app.route('/edit_user/<int:user_id>/', methods=["POST"])
def edit_user(user_id):
    data = {
        "id": user_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.edit(data)
    return redirect('/users')
@app.route('/users/<int:user_id>/destroy/', methods=['POST'])
def delete_user(user_id):
    data = {
        "id": user_id
    }
    User.delete_user_by_id(data)
    return redirect('/users')