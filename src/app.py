from flask import Flask, render_template , request , session , url_for
from src.calculator.rank import rank_calculate

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def hello():
    return render_template('calculate.html')

@app.route('/calculate', methods=['GET','POST'])
def calculate():
    letters=str(request.form['word'])

    rank=rank_calculate(letters)

    return render_template("calculate.html",wordie=letters , result=rank)


if __name__ == '__main__':
    app.run()
