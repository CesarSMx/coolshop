import sys
import csv
import os
 #add "changes in readme.md file" at next commit
CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['first_name', 'last_name', 'email', 'phone_number']

clients = []

def _initialize_clients_from_storage():
    # Opening .clients.csv file in reading mode and copying its actual
    # content to clients list variable.
    with open(CLIENT_TABLE, 'r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    # a temporary file is created with {}.temp
    tem_table_name = '{}.tmp'.format(CLIENT_TABLE)
    # save the changes made on clients list
    with open(tem_table_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        # clients.csv is replaced with the temporary file.
        os.remove(CLIENT_TABLE)
        os.rename(tem_table_name, CLIENT_TABLE)

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client is already in the client\'s list') 
    


def list_clients():
    global clients
    print("uid  |  first name   |   last_name  |  email  |  phone number")
    print("***********************************************************")
    # clients list is readed and content is printed row by row.
    for idx, client in enumerate(clients):
        print(f"{idx} | {client['first_name']} | {client['last_name']} | {client['email']} | {client['phone_number']}")


def update_client(client_name):
    global clients
    found = False
    for client in clients:
        if client['first_name'] == client_name:
            updated_client = _get_new_client_data()
            client['first_name'] = updated_client['first_name']
            client['last_name'] = updated_client['last_name']
            client['email'] = updated_client['email']
            client['phone_number'] = updated_client['phone_number']
            print('Client updated succesfully!')
            found = True
            break
    if not found:
        print(f'Client {client_name} does not exist')


def delete_client(client_name):
    global clients
    found = False
    for idx, client in enumerate(clients):
        if client['first_name'] == client_name:
            clients.pop(idx)
            found = True
            break
    if not found:
        print(f'Client {client_name} does not exist')


def search_client(client_name):
    global clients

    for client in clients:
        if client['first_name'] != client_name:
            continue
        else:
            return True


def _print_welcome_message():
    print('WELCOME TO COOLINK SHOP')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input(f"What's the client {field_name}: ")

    return field

def _get_client_name():
    client_name = None
    while client_name is None:
        client_name = input('What is the client name?: ')

        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name


def _get_new_client_data():
    client = {}
    client['first_name'] = _get_client_field("first_name")
    client['last_name'] = _get_client_field("last_name")
    client['email'] = _get_client_field("email")
    client['phone_number'] = _get_client_field("phone_number")

    return client


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome_message()
    
    command = input().lower()

    if command == 'c':
        client = _get_new_client_data()
        create_client(client)
    elif command == 'l':
        list_clients()
    elif command == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'u':
        client_name = _get_client_name()
        update_client(client_name)
    elif command == 's':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(f"Client {client_name} found")
        else:
            print(f'Client {client_name} was not found')
    else:
        print('Invalid command')
    
    _save_clients_to_storage()