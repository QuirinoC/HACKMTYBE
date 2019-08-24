import os

from flask import Flask, jsonify, make_response, request, render_template, Response, app

from flask_cors import CORS


#Flask stuff
app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {'db':'gorditos', 'alias':'default'}

@app.route("/", methods=['GET'])
def index():
    return jsonify({"usage": {
        "method" : "post", 
        "message" : "post an image"
    }})
@app.route('/classifier', methods=['POST'])
def classifier():
    return "HACKMTY"