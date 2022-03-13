from flask_restx import Namespace, Resource

from project.implemented import genre_service
from flask import request, jsonify
from project.helpers.decorators import admin_required
from project.schemas.schemas import GenreSchema



# @genres_ns.route("/<int:genre_id>")
# class GenreView(Resource):
#     @genres_ns.response(200, "OK")
#     @genres_ns.response(404, "Genre not found")
#     def get(self, genre_id: int):
#         """Get genre by id"""
#         try:
#             return GenresService(db.session).get_item_by_id(genre_id)
#         except ItemNotFound:
#             abort(404, message="Genre not found")


genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    #@auth_required
    def get(self):
        return jsonify(genres_schema.dump(genre_service.get_all()))

    @admin_required
    def post(self, user_id):
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{genre.id}/"}


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    #@auth_required
    def get(self, uid: int):
        return jsonify(genre_schema.dump(genre_service.get_one(uid)))

    @admin_required
    def put(self, user_id, uid: int):
        req_json = request.json
        genre_service.update(req_json, uid)
        return "", 204

    @admin_required
    def delete(self, user_id, uid: int):
        genre_service.delete(uid)
        return "", 204