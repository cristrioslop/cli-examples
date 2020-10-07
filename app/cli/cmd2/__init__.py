import click
from importlib import import_module


AVAILABLE_COMMANDS = ["sub1", "sub2"]


class CliTestSubCoreCLI(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(AVAILABLE_COMMANDS)

    def get_command(self, ctx, name):
        cmd2(ctx)  # warning! se llamaria por cada subcomando si no se especifica subcomando o si se hace --help
        name_sub = name.replace("-", "_")
        try:
            module = import_module(f"app.cli.cmd2.{name_sub}")
        except ModuleNotFoundError:
            raise click.UsageError(f"Invalid Command {name}")
        else:
            return getattr(module, 'main')

def cmd2(ctx):
    click.echo("Command 2")

main = CliTestSubCoreCLI()
