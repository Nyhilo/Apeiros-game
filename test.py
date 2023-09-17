# Sample game setup #

from apeiros import setup_database, create_player, get_player_name, check_square, \
    convert_png, autocrop


def printn(m):
    print('\n' + m)


# setup_database('sqlite:///db.sqlite3')
setup_database()

with open('test.jpg', 'rb') as f:
    player_image = f.read()


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
create_player(str(id), None, 'NewPlayer', player_image)
print('expected: NewPlayer got: ' + get_player_name(str(id)))

id += 1
create_player(None, 'newPlayer', 'NewPlayer', player_image)
print('expected: NewPlayer got: ' + get_player_name('newPlayer'))
