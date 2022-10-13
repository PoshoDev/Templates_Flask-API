import jwt
from functools import wraps
from flask import jsonify, request
from src import app, loaf

# Decorator for checking if a user is logged in.
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        #try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        uid = data['uid']
        #except:
        #    return Error.tokenInvalid()
        return f(uid, *args, **kwargs)
    return decorated

def verify(args, obligatory):
    if isinstance(obligatory, str):
        return obligatory in args
    for value in obligatory:
        if value not in args:
            return False
    return True