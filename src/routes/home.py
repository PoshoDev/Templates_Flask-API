from flask import jsonify
from src import app
from src.services.hello import say_hello

@app.route('/')
def home():
    return jsonify({'message': say_hello()})