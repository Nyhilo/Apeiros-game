from .database import Database
from .models import Player, Medal


class Game():
    def __init__(self, connectionString: str = 'sqlite+pysqlite:///:memory:') -> None:
        self.db = Database(connectionString)

    def test(self):
        # Create some dummy models
        


        nyhilo = Player(
            unique_id='00000016570670912',
            username='nyhilo',
            nickname='Nyhilo',
            medals=['participation_medal'],
            points=0,
            items={'treats': 10, 'moments': 20}
        )

        self.db.add_player(nyhilo)

        p = self.db.get_player('00000016570670912')
        print(p)
