# https://click.palletsprojects.com/en/7.x/commands/#custom-multi-commands
# cli with sub commands using custom load
# I think this is more flexible, scalable and clean that using command groups

import click
from importlib import import_module


AVAILABLE_COMMANDS = ["cmd1", "cmd2", "cmd3"]


class CliTestCoreCLI(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(AVAILABLE_COMMANDS)

    def get_command(self, ctx, name):
        name_sub = name.replace("-", "_")
        try:
            module = import_module(f"app.cli.{name_sub}")
        except ModuleNotFoundError:
            raise click.UsageError(f"Invalid Command {name}")
        else:
            return getattr(module, 'main')

main = CliTestCoreCLI()
