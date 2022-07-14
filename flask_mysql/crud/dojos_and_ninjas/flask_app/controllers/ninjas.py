from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninja_details():

    dojos = Dojo.get_all()

    return render_template("ninjaform.html", dojos=dojos)
@app.route('/create_ninja/', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/dojos')

