import click
from flask import url_for
import urllib.parse
from models.base import create_schema


def register_cli(app):
    @app.cli.command()
    def initdb():
        """Initialize the database."""
        click.echo('Init the database...')
        create_schema()

    @app.cli.command()
    def routes():
        """List all routes of app"""
        import urllib
        output = []
        for rule in app.url_map.iter_rules():

            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            line = urllib.parse.unquote("{:20s} {:40s} {}".format(rule.endpoint, methods, url))
            output.append(line)
