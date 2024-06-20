from flask import Flask, request

  


app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():

    some_code = request.form['code']
    html = eval(some_code)
    return html