def login(database, username, password):
    if username in database.keys() and password == database[username]:
        print(f'\nWelcome back {username}')
        return username
    elif username in database.keys() and password != database[username]:
        print('\nIncorrect password')
        return ''
    else:
        print('\nUser not found. Please register')
        return ''


def register(database, username):
    if username in database.keys():
        print('\nThat username is already registered')
        return ''
    else:
        print(f'\nuser {username} has been registered')
        return username
