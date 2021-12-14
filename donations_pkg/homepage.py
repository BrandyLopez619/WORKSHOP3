"""
main backend for donations page
"""


def show_homepage():
    """present main menu in app.py """
    print("")
    print("     === Automated Teller Machine ===     ")
    print("------------------------------------------")
    print("| 1.    Login    | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate   | 4.   Show Donations  |")
    print("-----------------------------------------")
    print("|               5. Exit                 |")
    print("-----------------------------------------")
    print("")


def donate(username):
    donation_amt = float(input('\nEnter amount to donate:'))
    print('\nThank you for your donation!')
    donation = (f'{username} donated ${donation_amt}')

    return donation
