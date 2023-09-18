from .game import db
from .models import Player
from .utilities import image


def create_player(
        unique_id: str | None,
        username: str | None,
        nickname: str | None,
        player_token: bytes,
        autocrop: bool = False
) -> Player:
    '''
    !! Use check_square() before submitting an image through this method. !!

    Create a new player in the database. unique_id, username, and nickname may
    be None, with some restrictions:

    Both a unique_id and username MAY be given (and SHOULD be if available),
    but one OR the other MUST be given.

    If a unique_id is given but a username is not, then a nickname MUST be.

    All values not specified MUST be given as None, for clarity.

    Args:
        unique_id (str | None):
            A unique internal ID, such as a discord User ID
        username (str | None):
            A unique username. Will be displayed when clarity between useres is
            desired.
        nickname (str | None):
            A nickname. Takes precedence over username for identifying the user.
        player_token (bytes):
            A square png. Maximum size of 200kb.

    '''
    # Sanitize identifiers
    unique_id, username, nickname = _handle_user_identifiers(unique_id, username, nickname)

    # Sanitize player token image
    player_token = _handle_player_token(player_token, autocrop)

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

    return player


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


# Written with Lily's help :)
def _handle_user_identifiers(unique_id: str, username: str, nickname: str) -> (str, str, str):
    has_unique_id = unique_id is not None
    has_username = username is not None
    has_nickname = nickname is not None

    match (has_unique_id, has_username, has_nickname):
        case (False, False, False):
            raise ValueError('Bro you didn\'t even give any ids. Why do you think those params are there?')
        case (_, False, False):
            raise ValueError('If a username is not given, a nickname must be provided to identify the player.')
        case (False, False, _):
            raise ValueError('Either a unique_id or a username must be given to create a new player.')
        case (False, True, _):
            unique_id = username
        case (_, True, False):
            nickname = username

    return (unique_id, username, nickname)


def _handle_player_token(token: bytes, autocrop: bool = False) -> bytes:
    # We'll just convert the image just to make sure
    token = image.convert_png(token)

    pixels_off, _ = image.check_square(token)
    if pixels_off > 0 and not autocrop:
        raise ValueError('Given player token image is not square.')

    if autocrop:
        return image.autocrop(token)

    return token
