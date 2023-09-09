from typing import List

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from .models import Base, Player, Medal


class Database():
    '''Contains game database interface methods.'''
    def __init__(self, connectionString: str) -> None:
        if connectionString is None:
            raise RuntimeError('No connection string provided.')

        self.engine = create_engine(connectionString)
        Base.metadata.create_all(self.engine)

        self.session = Session(self.engine)

    # Players #
    def add_player(self, player: Player) -> None:
        # Because of the way we're storing medals, the ids need to be updated first
        player.medal_ids = [m.medal_id for m in player.medals]
        self.session.add(player)

    def get_player(self, unique_id: str) -> Player:
        player = self.session.scalar(select(Player).where(Player.unique_id == unique_id))
        return self._populate_player_properties(player)

    def get_players(self, unique_ids: List[str] | None) -> List[Player]:
        players = None
        if unique_ids is None:
            players = self.session.scalars(select(Player)).all()

        elif type(unique_ids) is list:
            players = self.session.scalars(select(Player).where(Player.unique_id.in_(unique_ids))).all()

        # Because of the way we're storing the medal ids, they need to be added here
        return [self._populate_player_properties(player) for player in players]

    def _populate_player_properties(self, player: Player) -> None:
        medals = [self.get_medal(id) for id in player.medal_ids]
        player.medals = medals

    # Medals #
    def update_medal(self, medal: Medal) -> None:
        self.session.merge(medal)

    def get_medal(self, medal_id: str) -> Medal:
        return self.session.get(Medal, medal_id)

    def get_medals(self):
        return self.session.scalars(select(Medal)).all()
