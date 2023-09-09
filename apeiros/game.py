from .database import Database
from .models import Player, Medal


class Game():
    def __init__(self, connectionString: str = 'sqlite+pysqlite:///:memory:') -> None:
        self.db = Database(connectionString)

    def test(self):
        # Create some dummy models
        self.db.update_medal(Medal(medal_id='participation', name='Participation Medal', criteria='Join the game', number_available=50))
        self.db.update_medal(Medal(medal_id='cartographer', name='Cartographer Medal', criteria='Explore a bit', number_available=20))

        print('\nGET ALL MEDALS')
        print(self.db.get_medals())

        # Dummy player
        nyhilo = Player(
            unique_id='00000016570670912',
            username='nyhilo',
            nickname='Nyhilo',
            medals=['participation'],
            points=0,
            items={'treats': 10, 'moments': 20}
        )

        self.db.add_player(nyhilo)

        print('\nRE-GET AND PRINT PLAYER AND MEDALS')
        p = self.db.get_player('00000016570670912')
        m1 = self.db.get_medal(p.medals[0])
        print(p)
        print(m1)
