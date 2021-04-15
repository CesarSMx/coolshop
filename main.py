import sys

clients = [
    {
        "first_name": "Jose",
        "last_name": "Rosado",
        "email": "joser@email.com",
        "phone_number":"9954124595"
    },
    {
        "first_name": "Ricardo",
        "last_name": "Sanchez",
        "email": "ricardos@email.com",
        "phone_number":"9992657812"
    }
]


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client is already in the client\'s list') 
    


def list_clients():
    global clients
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
    _print_welcome_message()
    
    command = input().lower()

    if command == 'c':
        client = _get_new_client_data()
        create_client(client)
        list_clients()
    elif command == 'l':
        list_clients()
    elif command == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'u':
        client_name = _get_client_name()
        update_client(client_name)
        list_clients()
    elif command == 's':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(f"Client {client_name} found")
        else:
            print(f'Client {client_name} was not found')
    else:
        print('Invalid command')
