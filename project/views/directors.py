from flask_restx import Namespace, Resource

from project.implemented import director_service
from flask import request, jsonify
from project.helpers.decorators import auth_required, admin_required
from project.schemas.schemas import DirectorSchema


directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    #@admin_required
    def get(self):
        return jsonify(directors_schema.dump(director_service.get_all()))

    @admin_required
    def post(self, user_id):
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}/"}

@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, user_id, uid):
        return jsonify(director_schema.dump(director_service.get_one(uid)))

    @admin_required
    def put(self, user_id, uid: int):
        req_json = request.json
        director_service.update(req_json, uid)
        return "", 204

    @admin_required
    def delete(self, user_id, uid: int):
        director_service.delete(uid)
        return "", 204
