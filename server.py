import os

from flask import Flask, jsonify, make_response, request, render_template, Response

from flask_cors import CORS

@app.route('/classifier', methods=['GET'])
def classifier():
    return "OK"