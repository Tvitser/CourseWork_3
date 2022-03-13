from unittest.mock import Mock, patch

import pytest

from project.dao.models import Genre
from project.schemas.schemas import GenreSchema
from project.services.genres_service import GenreService


class TestGenresService:
    @pytest.fixture(autouse=True)
    def service(self, db):
        self.service = GenreService(db.session)

    @pytest.fixture
    def genre(self):
        return Genre(id=1, name="genre_1")

    @pytest.fixture
    def genre_dao_mock(self, genre):
        with patch("project.services.genres_service.GenreDAO") as mock:
            mock.return_value = Mock(
                get_by_id=Mock(return_value=GenreSchema().dump(genre))
            )
            yield mock

    def test_get_item_by_id(self, genre_dao_mock, genre):
        print(f"{dir(genre_dao_mock())}")


TestGenresService.test_get_item_by_id()