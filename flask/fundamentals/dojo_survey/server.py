from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe2'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/')
def display_results():
    print(session)
    return render_template('results.html', results=session)

@app.route('/collect_results/', methods=['POST'])
def collect_results():
    for key in request.form.keys():
        session[key] = request.form[key]
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)