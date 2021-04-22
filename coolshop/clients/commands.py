import click


@click.group()
def clients():
    """ Manage the clients lifecycle"""
    pass 


@clients.command()
@click.pass_context
def create(ctx, first_name, second_name, email, phone_number):
    """ Create a new client """
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


all = clients
 