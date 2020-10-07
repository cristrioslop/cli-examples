import click

from app.cli2.cmd2 import sub1
from app.cli2.cmd2 import sub2


@click.group()
def cmd2():
    click.echo("Command 2")

cmd2.add_command(sub1.sub1)
cmd2.add_command(sub2.sub2)