from .genres import genres_ns
from .directors import directors_ns
from .movies import movies_ns
from .users import users_ns, user_ns
from .auth import auth_ns
from .favorites import favorites_ns


__all__ = [
    "genres_ns","directors_ns","movies_ns","users_ns", "auth_ns", "user_ns", "favorites_ns"
]
