from flask import Flask, request, abort
from functools import wraps

def get_token_auth_header():
    # unpacking the request header
    if 'Authorization' not in request.headers:
        abort(401)
    
    auth_header = request.headers['Authorization']
    header_paths = auth_header.split(' ')

    if len(header_paths) != 2:
        abort(401)
    elif header_paths[0].lower() != 'bearer':
        abort(401)
    return header_paths[1]

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)
    return wrapper

app = Flask(__name__)

@app.route('/headers')
@requires_auth
def headers(jwt):
    
    print(jwt)
    return 'not implemented'

@app.route('/images')
@requires_auth
def images(jwt):
    
    print(jwt)
    return 'not implemented'