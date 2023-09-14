from .database import Database
from .models import Player, Medal, Item, Species, Nomster, NomsterType, NomsterClass, \
                    Location, LocationTag, Tile, Card, LocationProposal


class Game():
    def __init__(self, connectionString: str = 'sqlite+pysqlite:///:memory:') -> None:
        self.db = Database(connectionString)

    def test(self):
        # Create some dummy models
        self.db.upsert_medal(Medal(medal_id='participation', name='Participation Medal', criteria='Join the game', number_available=50))
        self.db.upsert_medal(Medal(medal_id='cartographer', name='Cartographer Medal', criteria='Explore a bit', number_available=20))

        print('\nGET ALL MEDALS')
        print(self.db.get_medal_list())

        participation_medal = self.db.get_medal('participation')

        # Dummy player
        nyhilo = Player(
            unique_id='00000016570670912',
            username='nyhilo',
            nickname='Nyhilo',
            medals=[participation_medal],
            points=0
        )

        print('\nSAVE PLAYER TO TABLE')
        self.db.add_player(nyhilo)

        print('\nRE-GET AND PRINT PLAYER AND MEDALS')
        p = self.db.get_player('00000016570670912')
        print(p)


        # Create some items
        self.db.upsert_item(Item(item_id='treat', name='Nomster Treat', description='A treat to bond with your Nomster!'))
        treat = self.db.get_item('treat')
        nyhilo.add_item(treat)
        print(nyhilo.get_slot('treat'))
        nyhilo.add_item(treat)
        nyhilo.add_item(treat)
        nyhilo.add_item(treat)
        print(nyhilo.get_slot('treat'))
        nyhilo.remove_item(treat)
        print(nyhilo.get_slot('treat'))
        nyhilo.remove_item(treat)
        nyhilo.remove_item(treat)
        nyhilo.remove_item(treat)
        print(nyhilo.get_slot('treat'))
        nyhilo.remove_item(treat)
        print(nyhilo.get_slot('treat'))

        print('\nCREATING NEW SPECIES')
        self.db.upsert_species(Species(nomster_type=NomsterType.Air, nomster_class=NomsterClass.Amphibian,
                                       name='Flying Frock', description='Dat frog got wings!'))
        flyingFrock = self.db.get_species_list()[0]
        print(flyingFrock)

        print('\nCREATE A WILD NOMSTER')
        frockus = Nomster(species=flyingFrock, location_x=0, location_y=0, is_tamed=False)
        print(frockus)

        print('\nTAME IT')
        frockus.is_tamed = True
        frockus.name = 'Frockus'
        nyhilo.nomsters.append(frockus)
        nyhilNomsters = self.db.get_player_nomsters(nyhilo)
        print(f'Nomsters owned by nyhilo: {nyhilNomsters}')
        print(f'owner: {nyhilNomsters[0].owner.nickname}')
        print(f'tamed?: {nyhilNomsters[0].is_tamed}')


        print('\nLOCATION TIME')
        apeiros = Location(
            name='Apeiros',
            details='Apeiros City',
            location_x=0,
            location_y=0,
            tile_image=Tile(image=b''),
            card_image=Card(image=b''),
            tile_submitter=nyhilo,
            submission_fulfiller=nyhilo,
        )
        apeiros.add_tag(LocationTag.Populated)
        apeiros.add_tag(LocationTag.Civilized)

        self.db.add_location(apeiros)
        ap2 = self.db.get_location(0, 0)
        print(ap2)
        print(ap2.get_tags())
