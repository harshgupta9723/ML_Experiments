from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return 'Home Page'

@app.route('/<string:name>/')
def name(name):
    return "Hello " + name + '!'

@app.route('/json', methods = ['GET'])
def json_resp():
    return jsonify(
        {'name' : 'Adam',
        'address' : 'London'})

if __name__ == '__main__' :
    app.run()