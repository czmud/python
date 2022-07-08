from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'is_game_over' not in session:
        session['game_message'] = ""
        session['is_game_over'] = False
        session['answer_val'] = random.randint(1,100)
        session['high'] = 100
        session['low'] = 1
        session['count'] = 0
    return render_template('index.html', game_message=session['game_message'], count=session['count'], \
        is_game_over=session['is_game_over'], high=session['high'], low=session['low'])

@app.route('/guess/', methods=['POST'])
def guess():
    guess = request.form['guess_val']
    if guess == "":
        guess = 0
    else:
        guess = int(guess)
    session['count'] +=1
    answer = session['answer_val']
    if guess == answer:
        session['game_message'] = f"{guess} is just right! You Win!"
        session['is_game_over'] = True
    elif session['count'] >= 5:
        session['game_message'] = "Too many guesses. You Lose."
        session['is_game_over'] = True
    else:
        if guess > answer:
            session['game_message'] = f"{guess} is too High!"
            if guess < session['high']:
                session['high'] = guess
        else:
            session['game_message'] = f"{guess} is too Low!"
            if guess > session['low']:
                session['low'] = guess

    return redirect('/')

@app.route('/reset/', methods=["POST"])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)