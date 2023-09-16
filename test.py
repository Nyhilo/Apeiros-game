# Sample game setup #

from apeiros import setup_database, create_player, get_player_name

# setup_database('sqlite:///db.sqlite3')
setup_database()

with open('test.png', 'rb') as f:
    player_image = f.read()

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
