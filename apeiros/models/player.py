from typing import Optional

from sqlalchemy import Integer, String, Binary
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


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
    player_token: Mapped[Optional[Binary]]

    # Medals owned by this player
    # TODO: This needs a relationship with a Medal class, or just a byteflag set if these are fungible
    # medals: Mapped[]

    # Currency, in the form of points.
    points: Mapped[int]

    # Items owned by this player. Individual items inherit from the Item class
    # TODO: This needs a relationship with an Item class, or just an id list if those are fungible
    # items: Mapped[]

    # The nomsters owned by this player
    # TODO: This needs a relationship with a Nomster class
    # nomsters: Mapped[]
