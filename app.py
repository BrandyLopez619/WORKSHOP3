"""
logic for donations_pkg
"""
from donations_pkg.homepage import show_homepage, donate
from donations_pkg.user import login, register

database = {'admin': 'pass123', 'brandy': 'pass321'}
donations = []
authorized_user = ''
totals = []

while True:
    show_homepage()
    if authorized_user == '':
        print('You must be logged in to donate\n')
    else:
        print(f'Logged in as {authorized_user}\n')
    option = input('Please select an option: ')
    if option == '1':
        username = input('\nEnter Username: ').lower()
        password = input('Enter Password: ')
        authorized_user = login(database, username, password)
    elif option == '2':
        while True:
            username = input('\nEnter Username: ').lower()
            password = input('Enter Password: ')
            if len(username) > 10:
                print("username must be under 10 characters long")
            elif len(password) < 5:
                print("password must be atleast 5 characters long")
            else:
                authorized_user = register(database, username)
                if authorized_user != '':
                    database[username] = password
                break
    elif option == '3':
        if authorized_user == '':
            print('You are not logged in')
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif option == '4':
        if [] in donations:
            print('\nCurrently, there are no donations.')
        else:
            print('\n--- All Donations ---')
            for entry in donations:
                print(entry)
            for entry in donations:
                dollar = entry.find('$')
                cash = float(entry[dollar+1:])
                totals.append(cash)
            print('Total donations = $', sum(totals))

    elif option == '5':
        print('\nLeaving DonateMe...')
        break
