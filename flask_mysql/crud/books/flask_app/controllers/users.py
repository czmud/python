from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user
from flask_app.models import favorite


@app.route('/')
@app.route('/authors/')
def index():
    users = user.User.get_all()
    return render_template("index.html", users=users)
@app.route('/authors/<int:user_id>')
def show_author(user_id):
    data = { "id": user_id }
    users = user.User.get_user_by_id(data)
    return render_template("authorshow.html", users=users)
@app.route('/create_author/', methods=["POST"])
def create_author():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    user.User.save(data)
    return redirect('/authors')
@app.route('/add_favorite', methods=["POST"])
def add_favorite():
    data = {
        "user_id": request.form["user_id"],
        "book_id": request.form["book_id"]
    }
    favorite.Favorite.save(data)
    return redirect('authors/'+data['user_id'])
