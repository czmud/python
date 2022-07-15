from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/')
def display_results():
    data = {
        "id": session["survey_id"]
    }
    survey = Survey.get_survey_by_id(data)
    return render_template('results.html', survey=survey, session=session)

@app.route('/collect_results/', methods=['POST'])
def collect_results():
    if not Survey.validate_survey(request.form):
        session["name"]= request.form["name"]
        session["location"]= request.form["location"]
        session["language"]= request.form["language"]
        session["comment"]= request.form["comment"]
        return redirect('/')
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"], 
    }
    session.clear()
    session['survey_id'] = Survey.save(data)
    return redirect('/results')