from flask import Flask, Blueprint
from flask_restful import Api
import logging
from time import time
from flask import request
from configs.config import LOGGING
from logging.config import dictConfig
from flask import got_request_exception
from base.utils import get_client_ip
from flask_sqlalchemy import SQLAlchemy

dictConfig(LOGGING)
request_logger = logging.getLogger("api.request")

app = Flask("{{cookiecutter.project_slug}}")
app.config.from_pyfile('configs/config.py')

db = SQLAlchemy(app)

api_bp = Blueprint('api', __name__, url_prefix='/v1')
api = Api(api_bp)

# Routers
from resources.user import UserResource

api.add_resource(UserResource, '/users')

app.register_blueprint(api_bp)

# Custom CLI
from cli import register_cli

register_cli(app)


# Middleware
@app.before_request
def before_request():
    request.start_time = time()


@app.after_request
def after_request(response):
    log_format = '{ip} "{user_agent}" {method} {path} {status_code} {response_time:.3f}'

    data = {
        "ip": get_client_ip(request),
        "user_agent": request.headers.get('User-Agent'),
        "method": request.method,
        "path": request.full_path,
        "status_code": response.status_code,
        "response_time": time() - request.start_time
    }
    request_logger.info(log_format.format(**data))
    return response


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.exception(exception)


got_request_exception.connect(log_exception, app)

if __name__ == '__main__':
    app.run(debug=False)
