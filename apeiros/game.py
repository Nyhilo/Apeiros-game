from .database import Database
from .models import Player, Medal, Item


class Game():
    def __init__(self, connectionString: str = 'sqlite+pysqlite:///:memory:') -> None:
        self.db = Database(connectionString)

    def test(self):
        pass
