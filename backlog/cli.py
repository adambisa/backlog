import typer
from backlog import __app_name__, __version__, database

app = typer.Typer()
app_backlog = database.Backlog()


@app.command()
def add(task):
    app_backlog.push(task)
    typer.echo(f"Task '{task}' added successfully")


@app.command()
def remove():
    app_backlog.pop()
    typer.echo(f"Task removed successfully")


@app.command()
def list_tasks():
    typer.echo(app_backlog.show())


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
        version: bool = typer.Option(
            None,
            "--version",
            help="Show version and exit",
            callback=version_callback,
            is_eager=True
        )
) -> None:
    return
