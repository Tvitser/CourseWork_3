
import pytest

class TestGenreDAO:
    @pytest.fixture(autouse=True)
    def dao(self, genre_dao_test):
        self.dao = genre_dao_test


    def test_get_genre_by_id(self):
        genre = self.dao.get_one(1)
        assert genre != None
        assert genre.id != None


    def test_get_all_genres(self):
        genres = self.dao.get_all()
        assert len(genres) > 0
