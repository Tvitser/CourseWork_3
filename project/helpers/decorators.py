from flask import request, abort

from project.services.Jwt_token import JwtToken
from project.services.enums import UserRole


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        token = data.split("Bearer ")[-1]
        try:
            user = JwtToken.decode_token(token)
            if user['role'] != UserRole.admin:
                abort(403)
            return func(*args, **kwargs, user_id=user['user_id'])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):
        user = None
        data = request.headers.get('Authorization')
        if 'Authorization' not in request.headers:
            abort(401)
        token = data.split("Bearer ")[-1]
        try:
            user = JwtToken.decode_token(token)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs, user_id=user['user_id'])
    return wrapper