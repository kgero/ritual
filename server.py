import json
import random

from flask import Flask, Response, render_template, request


app = Flask(__name__)

feelings = []

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/getfeeling', methods=['POST'])
def getfeeling():
    if len(feelings) > 0:
        out = random.choice(feelings)
    else:
        out = []
    feelings.append(request.form['body'])
    print(len(feelings))
    print(feelings)
    resp = Response(out, status=200, mimetype='application/json')

    return resp
