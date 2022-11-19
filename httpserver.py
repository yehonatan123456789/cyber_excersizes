from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(request.args['a'])
    print(int(request.args['a']) + int(request.args['b']))
    return "<p>the result of {} + {} is {} </p>".format(request.args['a'], request.args['b'], int(request.args['a']) + int(request.args['b'] ))
