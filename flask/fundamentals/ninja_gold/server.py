from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'ninja gold 986102987569830246'

@app.route('/')
def index():
    if 'activity_log' not in session:
        session['activity_log'] = []
        session['gold_sum'] = 0
    
    return render_template('index.html', session=session)

@app.route('/process_money/', methods=['POST'])
def process_money():
    gold_dict = {
        'farm': {'gold_low': 10, 'gold_high': 20},
        'cave': {'gold_low': 5, 'gold_high': 10},
        'house': {'gold_low': 2, 'gold_high': 5},
        'casino': {'gold_low': -50, 'gold_high': 50}
    }
    gold_act = request.form['gold_action']
    gold_added = yield_gold(gold_dict[gold_act]['gold_low'], gold_dict[gold_act]['gold_high'])
    session['gold_sum'] += gold_added
    if gold_added == 0:
        session['activity_log'].append('No gold earned')
    elif gold_added < 0:
        session['activity_log'].append(f'Entered a {gold_act.title()} and lost {-gold_added} gold... Ouch.')
    else:
        session['activity_log'].append(f'Earned {gold_added} gold from the {gold_act.title()}!')

    print(gold_act)
    print(gold_added)
    print(session['gold_sum'])
    return redirect('/')

def yield_gold(gold_low, gold_high):
    gold_val = random.randint(gold_low, gold_high)
    return gold_val


@app.route('/reset/', methods=["POST"])
def destroy_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)