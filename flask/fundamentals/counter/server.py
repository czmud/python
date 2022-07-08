from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'visit_count' not in session:
        session['visit_count'] = 0
    else: 
        session['visit_count'] += 1
    if 'count' not in session:
        session['count'] = 0
    else: 
        session['count'] += 1
    return render_template('index.html', count=session['count'], visit_count=session['visit_count'])

@app.route('/increment/', methods=["POST"])
def increment_counter():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session/', methods=["POST"])
def destroy_session():
    session.pop('count')
    return redirect('/')

@app.route('/set_counter/', methods=["POST"])
def set_counter():
    count = int(request.form["count_val"])
    session['count'] = count - 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)