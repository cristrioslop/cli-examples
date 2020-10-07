# https://click.palletsprojects.com/en/7.x/commands/#callback-invocation
# cli with sub commands using command groups

import click

from app.cli2 import cmd1
from app.cli2 import cmd2
from app.cli2 import cmd3


@click.group()
def main():
    click.echo("cli")

main.add_command(cmd1.cmd1)
main.add_command(cmd2.cmd2)
main.add_command(cmd3.cmd3)
