from src import app, loaf
from src.services.access import token_required, verify

import jwt
from flask import jsonify, request

# Login function. Returns a token.
@app.route('/login', methods=['POST'])
def api_login():
    if request.method == 'POST':
        print(request.args)
        # Sanity check.
        if not verify(request.args, ['username', 'password']):
            return jsonify({"message":"Missing username or password."}), 400
        username = request.args['username']
        password = request.args['password']
        uid = 1
        token = jwt.encode({'uid': uid}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({
            'token': token,
            'message': 'Logged in successfully!'
        }), 200