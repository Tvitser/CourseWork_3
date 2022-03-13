from flask_restx import  Namespace, Resource

from project.implemented import movie_service
from flask import request, current_app
from project.helpers.decorators import auth_required, admin_required
from project.schemas.schemas import MovieSchema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    #@auth_required
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        status = request.args.get("status")
        page_index = request.args.get("page")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
            'status': status,
            'page': page_index
        }
        page_size = current_app.config['ITEMS_PER_PAGE']
        all_movies = movie_service.get_all(filters, page_size)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @admin_required
    def post(self, user_id):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movies_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, user_id, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, user_id, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, user_id, bid):
        movie_service.delete(bid)
        return "", 204
