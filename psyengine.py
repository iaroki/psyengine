#!/usr/bin/env python3

import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/psyanimal', methods=['POST', 'GET'])
def psyanimal():
    with open('questions.json', 'r') as jsonfile:
        questions_dict = json.load(jsonfile)

    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        data = request.form.getlist('question')
        return render_template('psyanimal_response.html', name=name, desc=desc, data=data, questions_dict=questions_dict)

    return render_template('psyanimal_index.html', questions_dict=questions_dict)

