from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success/')
def email_success():
    if 'email_id' not in session:
        return redirect('/')
    emails = email.Email.get_all()
    
    return render_template("success.html", emails=emails)


@app.route('/add_email', methods=["POST"])
def add_new_email():
    if not email.Email.validate_email(request.form):
        session["email_login"] = request.form["email"]
        return redirect('/')
    
    data = { "email": request.form["email"] }
    session.clear()
    session["email_id"] = email.Email.save(data)
    return redirect('/success')

@app.route('/logout/')
def log_email_out():
    session.clear()
    return redirect('/')

@app.route('/delete/<int:email_id>', methods=["POST"])
def delete_email(email_id):
    if 'email_id' in session:
        if email_id == session['email_id']:
            session.clear()
    data = { "id": email_id }
    email.Email.delete_email_by_id(data)
    return redirect('/success')
