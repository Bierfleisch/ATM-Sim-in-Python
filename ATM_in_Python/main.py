import json
from os.path import exists
from shutil import copyfile


def create_account(filename):
    source = 'template.json'
    destination = f'Accounts/{filename}.json'
    copyfile(source, destination)


def load_account(account_name):
    path = f'Accounts/{account_name}.json'

    path_exits = exists(path)

    if not path_exits:
        create_account(account_name)

    with open(path, 'r') as file:
        # load the json file and convert to python dictionary
        account = json.load(file)

        if not path_exits:
            # if the dictionary was just created set the filename inside the file
            account['accountName'] = account_name

        return account


def save_account(account):
    with open(f'Accounts/{account["accountName"]}.json', 'w') as file:
        # json.dump == convert python dictionary to file
        json.dump(account, file)


if __name__ == '__main__':
    person1_account = load_account('Person1')
    person1_account['balance'] = 1000000000
    person1_account['balance'] -= 100
    save_account(person1_account)
