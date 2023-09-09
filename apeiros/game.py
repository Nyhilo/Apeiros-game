from .database import Database


class Game():
    def __init__(self, connectionString: str = 'sqlite+pysqlite:///:memory:') -> None:
        self.db = Database(connectionString)

    def test():
        print('Test string.')
