import logging
from logging.config import dictConfig
from flask import got_request_exception
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from objects import app

from configs.config import LOGGING
from api import register_api
from cli import register_cli
from middlewares import request_logging

# Trick: call app.logger before config app.logger by dictConfig.
app.logger.info("Init flask app ...")
dictConfig(LOGGING)
request_logger = logging.getLogger("api.request")

# Init JWT
jwt = JWTManager(app)

# Init API
register_api(app)

# Allow CORS
CORS(app)

# Register custom CLI
register_cli(app)

# Register middleware
request_logging.register_middleware(app)


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.exception(exception)


got_request_exception.connect(log_exception, app)

if __name__ == '__main__':
    app.run(debug=False)
