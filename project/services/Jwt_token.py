from calendar import timegm
from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from flask import current_app
from project.schemas.schemas import JwtSchema


class JwtToken:
    def __init__(self, data: Dict[str, Any]):
        self._now = datetime.now()
        self.__schema = JwtSchema()
        self._data = self.__schema.load(self.__schema.dump(data))
        self._access_token_expiration = 10  # minutes
        self._refresh_token_expiration = 30  # days

    def _get_token(self, time_delta: timedelta) -> str:
        self._data.update({
            "exp": timegm((self._now + time_delta).timetuple())
        })
        return jwt.encode(
            payload=self.__schema.dump(self._data),
            key=current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )

    def _refresh_token(self) -> str:
        return self._get_token(time_delta=timedelta(days=self._refresh_token_expiration))

    def _access_token(self) -> str:
        return self._get_token(time_delta=timedelta(minutes=self._access_token_expiration))

    def get_tokens(self) -> Dict[str, str]:
        return {
            "access_token": self._access_token(),
            "refresh_token": self._refresh_token(),
        }

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        return JwtSchema(exclude=('exp',), unknown='PASS').load(
            data=jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        )
