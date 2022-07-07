from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={'num': 0, 'color':"pink"})
@app.route('/play/', defaults={'num': 3, 'color':"pink"})
@app.route('/play/<int:num>/', defaults={'color':"blue"})
@app.route('/play/<int:num>/<color>/')
def play1(num, color):
    return render_template("index.html", block_color=color, block_count=num)

if __name__=="__main__":
    app.run(debug=True, port=5000)