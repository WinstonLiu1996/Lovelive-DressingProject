from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
from flask import flash

import json

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'lovelive!ubc-cs-idol-project'

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
@app.route('/<name>')
def index(name="Winston"):
    data = get_saved_data()
    return render_template("index.html", saves=data, name=name)

@app.route('/builder')
def builder():
    return render_template('builder.html', saves=get_saved_data(), options=DEFAULTS)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    #flask only can return string: return str(num1+num2)
    return render_template("add.html", num1=num1, num2=num2)


@app.route('/save', methods=['POST'])
def save():
    flash("ありがとうございました! Thank you for Update!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response

app.run(debug=True, port=8000, host='0.0.0.0')

#render template
