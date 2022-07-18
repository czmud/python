from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/login/')
def display_user():
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id": session["user_id"]
    }
    user = User.get_user_by_id(data)
    return render_template("userpage.html", user=user)

@app.route('/user_login/', methods=['POST'])
def log_user_in():
    if not User.validate_login(request.form):
        session['email_login'] = request.form['email']
        return redirect('/')
    data = {
        "email": request.form["email"]
    }

    user = User.get_user_by_email(data)
    session.clear()
    session["user_id"] = user.id

    return redirect('/login')

@app.route('/create_user/', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        session["first_name"]= request.form["first_name"]
        session["last_name"]= request.form["last_name"]
        session["email"]= request.form["email"]
        return redirect('/')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    data['salt'] = User.generate_salt()
    data['password_hash'] = User.hash_password(request.form, data['salt'])
    session.clear()
    session['user_id'] = User.save(data)
    return redirect('/login')

@app.route('/user_logout/')
def log_user_out():
    session.clear()
    return redirect('/')