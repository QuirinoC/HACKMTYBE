import os

from flask import Flask, jsonify, make_response, request, render_template, Response, app

from flask_cors import CORS

from predictor import predict

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

    req = request.form or request.json

    img = request.files.get("image")

    if not img:
        return jsonify({
            "status" : "error",
            "message" : "Image not found in request"
        })

    tag, confidence = predict(img)

    return jsonify(
        {
        "image" : img.filename,
        "tag" : tag,
        "confidence" : confidence
        }
    )