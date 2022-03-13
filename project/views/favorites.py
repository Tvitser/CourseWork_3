from flask_restx import Resource, Namespace

from project.helpers.decorators import auth_required
from project.implemented import user_movie_service, movie_service
from project.schemas.schemas import UserMovie, MovieSchema

favorites_ns = Namespace('favorites')
users_movie = UserMovie(many=True)
movies_schema = MovieSchema(many=True)

@favorites_ns.route('/movies/')
class FavView(Resource):
    @auth_required
    def get(self, user_id: int):
        fav = movie_service.get_fav(user_id)
        return movies_schema.dump(fav)


@favorites_ns.route('/movies/<int:movie_id>')
class FavView(Resource):
    @auth_required
    def delete(self, user_id: int, movie_id: int):
        movie_service.get(user_id, movie_id)
        return "", 204

    @auth_required
    def post(self, user_id: int, movie_id: int):
        user_movie_service.create({'user_id': user_id, 'movie_id': movie_id})
        return "", 204
