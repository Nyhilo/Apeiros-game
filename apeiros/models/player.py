from typing import Optional, List, Dict, Any

from sqlalchemy import BLOB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Player(Base):
    __tablename__ = 'apeiros_players'

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Client specific unique id such as a discord user ID, or generated id
    # If no alternate unique id is available, this should be the same as username
    unique_id: Mapped[str]

    # User identifying names that will be rendered to the user
    username: Mapped[str]
    nickname: Mapped[Optional[str]]

    # A png byte blob
    player_token = mapped_column(type_=BLOB, nullable=True)

    # Medal ids owned by this player. Is stored as a comma-separated list of ids
    _medals: Mapped[str] = mapped_column('medals')

    @property
    def medals(self) -> List[str]:
        return self._medals.split(',')

    @medals.setter
    def medals(self, medals) -> None:
        # Sanitize ids for characters that are used in storage
        for medal in medals:
            if ',' in medal:
                raise ValueError('Detected comma in medals list. Couldn\'t store list in database.')

        self._medals = ','.join(medals)

    # Currency, in the form of points.
    points: Mapped[int]

    # Items owned by this player. This is a dictionary with item_ids as keys and the amount owned as values
    _items: Mapped[str] = mapped_column('items')

    @property
    def items(self) -> Dict[str, int]:
        pairs = self._items.split(',')
        split_pairs = [pair.split(':') for pair in pairs]

        return {pair[0]: int(pair[1]) for pair in split_pairs}

    @items.setter
    def items(self, items):
        # Sanitize ids for characters that are used in storage
        for key in items:
            if ',' in key:
                raise ValueError(f'Detected comma in items key "{key}". Couldn\'t store dictionary in database.')

            if ':' in key:
                raise ValueError(f'Detected colon in items key "{key}". Couldn\'t store dictionary in database.')

        self._items = ','.join(f'{k}:{v}' for k, v in items.items())

    # The nomsters owned by this player
    # TODO: This needs a relationship with a Nomster class
    # nomsters: Mapped[]

    def __repr__(self) -> str:
        return (
            f'Player(id={self.id!r}, unique_id={self.unique_id!r}, username={self.username!r}, '
            f'nickname={self.nickname!r}, _medals={self._medals!r}, points={self.points!r}, _items={self._items!r})'
        )
