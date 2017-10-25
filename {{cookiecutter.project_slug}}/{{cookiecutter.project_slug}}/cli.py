import click
from models.base import create_schema


def register_cli(app):
    @app.cli.command()
    def initdb():
        """Initialize the database."""
        click.echo('Init the database...')
        create_schema()
