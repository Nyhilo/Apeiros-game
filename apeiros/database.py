from typing import List

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from .player import Player


class Base(DeclarativeBase):
    pass


class Database():
    '''Contains game database interface methods.'''
    def __init__(self, connectionString: str) -> None:
        if connectionString is None:
            raise RuntimeError('No connection string provided.')

        self.engine = create_engine(connectionString)
        Base.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)

    # Players #
    def add_player(self, player: Player):
        self.session.add(player)

    def get_player(self, unique_id: str) -> Player:
        return self.session.scalar(select(Player).where(Player.unique_id == unique_id))

    def get_players(self, unique_ids: List[str] | None) -> List[Player]:
        if unique_ids is None:
            return self.session.scalars(select(Player)).all()

        elif type(unique_ids) is list:
            return self.session.scalars(select(Player).where(Player.unique_id.in_(unique_ids))).all()
