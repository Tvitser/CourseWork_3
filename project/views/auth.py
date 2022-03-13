from flask_restx import Resource, Namespace
from project.implemented import user_service
from flask import request, abort

from project.schemas.schemas import UserSchema
from project.services import JwtToken
from project.tools.security import compare_passwords

auth_ns = Namespace('auth')

# register /auth/register
@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        data = UserSchema().load(req_json, many=None)
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}

@auth_ns.route('/login')
class AuthView(Resource):
    # login /auth/login
    def post(self):
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            abort(400)
        user = user_service.get_by_email(email)
        if not user or not compare_passwords(user.password, password):
            abort(401)
        tokens = JwtToken({'user_id': user.id, 'role': user.role}).get_tokens()
        user_service.update(tokens, user.id)
        return tokens, 201

    #обновить Refresh_token
    def put(self):
        refresh_token = request.json.get("refresh_token")
        data = JwtToken.decode_token(refresh_token)
        user_id = data.get("user_id")
        user = user_service.get_one(user_id)
        tokens = JwtToken({'user_id': user.id, 'role': user.role}).get_tokens()
        user_service.update(tokens, user.id)
        return tokens, 201
