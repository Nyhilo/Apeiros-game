# Sample game setup #

from apeiros import setup_database, create_player, get_player_name, check_square, \
    convert_png, autocrop, create_location, create_location_proposal
from apeiros.exceptions import LocationOverlapError


def printn(m):
    print('\n' + m)


# setup_database('sqlite:///db.sqlite3')
setup_database()

with open('test.jpg', 'rb') as f:
    player_image = f.read()

with open('location.webp', 'rb') as f:
    location_image = f.read()


printn('Ensure that the player image is a png')
player_image = convert_png(player_image)

printn('Check the squareness of test.jpg')
pixels, percent = check_square(player_image)
print(f'{pixels=}, {percent=}')

printn("If it's not square, try to auto-crop it.")
if pixels > 0:
    print('Cropping!')
    player_image = autocrop(player_image)


printn('Let\'s try some player id lookups.')
id = 1
create_player(str(id), 'newPlayer', 'NewPlayer', player_image)
print('expected: NewPlayer got: ' + get_player_name(str(id)))

id += 1
create_player(str(id), 'newPlayer', None, player_image)
print('expected: newPlayer got: ' + get_player_name(str(id)))

id += 1
player_a = create_player(str(id), None, 'NewPlayer', player_image)
print('expected: NewPlayer got: ' + get_player_name(str(id)))

id += 1
player_b = create_player(None, 'newPlayer', 'NewPlayer', player_image)
print('expected: NewPlayer got: ' + get_player_name('newPlayer'))

printn('Try changing the nickname.')
player_b.nickname = 'NewNickName'
print('expected: NewNickName got: ' + get_player_name('newPlayer'))

printn('Create a new location')
try:
    proposal = create_location_proposal(player_a, location_image)
    myloc = create_location(0, 0, 'Apeiros Town', 'The home of Inifinite Nomic', proposal, player_b)
except LocationOverlapError:
    print('Location overlap found.')
