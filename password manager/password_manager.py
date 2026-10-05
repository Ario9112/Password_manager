accounts = list()

def add_password():
    website = input("Please enter website: ")
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    category = input("Please enter category: ")
    note = input("Please enter note: ")

    account = {
        'website' : website,
        'username' : username,
        'password' : password,
        'category' : category,
        'note' : note, 
    }

    accounts.append(account)
    print("New account data was added!")

def view_accounts():
    if len(accounts) <= 0 :
        print('Account list is empty!')
    else:
        for i, data in enumerate(accounts, 1):
            print(f"{i}. website: {data['website']}")
            print(f"   username: {data['username']}")
            print(f"   password: {data['password']}")
            print(f"   category: {data['category']}")
            print(f"   note: {data['note']}\n")

def edit_accounts():
    view_accounts()

    try:
        select = int(input('Select an account: '))
    except ValueError:
        print('Please enter a valid account number.')
        return

    if 0 < select <= len(accounts):
        website = input("Please enter website: ")
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        category = input("Please enter category: ")
        note = input("Please enter note: ")

        new_accounts = {
            'website' : website,
            'username' : username,
            'password' : password,
            'category' : category,
            'note' : note, 
        }

        accounts[select-1] = new_accounts
    else:
        print('Account number is out of range.')

def password_generator(length=12):
    import random
    import string

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def delete_account():
    view_accounts()

    try:
        select = int(input('Select an account: '))
    except ValueError:
        print('Please enter a valid account number.')
        return

    if 0 < select <= len(accounts):
        accounts.pop(select-1)
        print('Account deleted.')
    else:
        print('Account number is out of range.')




def main():
    while True:
        choice = input("Please choose an option (1: add, 2: view, 3: edit, 4: delete, q: quit): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            edit_accounts()
        elif choice == "4":
            delete_account()
        elif choice.lower() == "q":
            break
        else:
            print("Invalid option.")

main()


