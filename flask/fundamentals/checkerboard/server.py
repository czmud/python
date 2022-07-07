from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/', defaults={'x':8, 'y':8})
@app.route('/play/<int:x>/', defaults={'y':8})
@app.route('/play/<int:x>/<int:y>/')
def checkers(x, y):
    # generates a checkerboad with dimensions 'x' by 'y' 
    # and alternating color squares determined by using mod 2 of x + y
    checker_grid = []
    # first loop generates rows
    for i in range(y):
        checker_row = []
        # second generates columns
        for j in range(x):
            if (i+j) % 2 == 0:
                checker_row.append('block-even')
            else:
                checker_row.append('block-odd')
        checker_grid.append(checker_row)
    return render_template("index.html", checker_grid=checker_grid)

if __name__=="__main__":
    app.run(debug=True)