import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """ Manage the clients lifecycle"""
    pass 


@clients.command()
@click.pass_context
@click.option('-n', '--first_name', type=str, prompt=True, help='The client first name')
@click.option('-l', '--last_name', type=str, prompt=True, help='The client last name')
@click.option('-e', '--email', type=str, prompt=True, help='The clients email')
@click.option('-n', '--phone_number', type=str, prompt=True, help='The client phone number')
def create(ctx, first_name, last_name, email, phone_number):
    """ Create a new client """
    client = Client(first_name, last_name, email, phone_number)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list =  client_service.list_clients()
    click.echo('  ID  |  First Name  |  Last Name  |  Email  |  Phonenumber  ')
    click.echo('*' * 100)
    for client in clients_list:
        click.echo('{uid}  |  {first_name}  |  {last_name}  |  {email}  |  {phone_number}'.format(
            uid = client['uid'],
            first_name = client['first_name'], 
            last_name = client['last_name'],
            email = client['email'],
            phone_number = client['phone_number']
        ))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        #update floww
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')

    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')
    client.first_name = click.prompt('New first name', type=str, default=client.first_name)
    client.last_name = click.prompt('New last name', type=str, default=client.last_name)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.phone_number = click.prompt('New phone number', type=str, default=client.phone_number)
    return client

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]
    if client:
        client_service.delete(Client(**client[0]))
        click.echo('Client deleted')
    else:
        click.echo('Client not found')




all = clients
 