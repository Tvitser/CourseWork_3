import os

from project.implemented import movie_service
from tests.acess_ import access_token


class TestGenresView:
    url = "/movies/"

    def test_get_movies(self, client):
        response = client.get(self.url, headers={'Authorization': access_token})
        assert response.status_code == 200
        page_size = 3
        filters = {}
        movie = movie_service.get_all(filters, page_size).all()
        assert len(movie) == 20, f'len(movie) должно быть равно 20, а равно {len(movie)}'




if __name__ == "__main__":
    os.system("pytest")
