from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
@app.route('/dojos/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)
@app.route('/create_dojo/', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def dojo_members(dojo_id):
    data = {
        'id': dojo_id
    }

    dojo = Dojo.get_dojo_by_id(data)
    return render_template("dojomembers.html", dojo=dojo)