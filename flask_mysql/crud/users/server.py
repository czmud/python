from flask import Flask, render_template, redirect, request, session

from user import User
app = Flask(__name__)
@app.route('/users/')
def index():
    users = User.get_all()
    print(users)
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

if __name__ == "__main__":
    app.run(debug=True)