from flask import Flask
import logging
from configs.config import LOGGING
from logging.config import dictConfig
from flask import got_request_exception
from flask_sqlalchemy import SQLAlchemy

app = Flask("{{cookiecutter.project_slug}}")
app.config.from_pyfile('configs/config.py')

# Trick: call app.logger before config app.logger by dictConfig.
app.logger.info("Init flask app ...")
dictConfig(LOGGING)
request_logger = logging.getLogger("api.request")

# Init db
db = SQLAlchemy(app)

# Init API
from api import api_bp

app.register_blueprint(api_bp)

# Register custom CLI
from cli import register_cli

register_cli(app)

# Register middleware
from middlewares import request_logging

request_logging.register_middleware(app)


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.exception(exception)


got_request_exception.connect(log_exception, app)

if __name__ == '__main__':
    app.run(debug=False)
