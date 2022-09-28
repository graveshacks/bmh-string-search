from urllib import request
from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        text = request.form['text']
        pattern = request.form['pattern']
        s = main.BoyerMooreHorspool(pattern,text)
        result = 'Pattern \"' + pattern + '\" found at position '+str(s)
        return result
    return render_template('index.html', result = result)

if __name__=='__main__':
    app.run(debug=True, port=2025)
