from flask import jsonify
from src import app
from src.services.access import token_required
from src.services.hello import say_hello

@app.route('/')
@token_required
def home():
    return jsonify({'message': say_hello()})