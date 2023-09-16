from .game import db
from .models import Player
from .utilities.image import check_square


def create_player(
        unique_id: str | None,
        username: str | None,
        nickname: str | None,
        player_token: bytes
) -> None:
    '''
    !!Use check_square() before submitting an image through this method.!!
    Create a new player in the database. unique_id, username, and nickname may
     be None, with some restrictions:
    Both a unique_id and username MAY be given (and SHOULD be if available),
     but one OR the other MUST be given.
    If a unique_id is given but a username is not, then a nickname MUST be.
    All values not specified MUST be given as None, for clarity.

    Args:
        unique_id (str | None): A unique internal ID, such as a discord User ID
        username (str | None):  A unique username. Will be displayed when
                                 claridy between useres is desired.
        nickname (str | None):  A nickname. Takes precedence over username for
                                 identifying the user.
        player_token (bytes):   A square png. Maximum size of 200kb.
    '''
    # Sanitization
    if unique_id is None and username is None:
        raise ValueError('Either a unique_id or a username must be given to create a new player.')

    if unique_id is not None and username is None and nickname is None:
        raise ValueError('If a username is not given, a nickname must be provided to identify the player.')

    if unique_id is None and username is not None:
        unique_id = username

    if nickname is None and username is not None:
        nickname = username

    pixels_off, _ = check_square(player_token)
    if pixels_off != 0:
        raise ValueError('Given player token image is not square.')

    player = Player(
        unique_id=unique_id,
        username=username,
        nickname=nickname,
        player_token=player_token,
        points=0,
        medals=[],
        inventory=[],
        nomsters=[]
    )
    db().add_player(player)


def get_player_name(unique_id: str) -> str:
    '''
    Gets the identifying name of a player, either its nickname or username.

    Args:
        unique_id (str): The unique id of a player object. This value is
                            usually an arbitrary id set by the calling client,
                            but may be a username is another id was not
                            provided.

    Returns:
        str: The human-readable identifying string of the player.
    '''
    player = db().get_player(unique_id)

    if player is None:
        raise LookupError('No player found with that unique id.')

    if player.nickname is not None:
        return player.nickname

    return player.username
