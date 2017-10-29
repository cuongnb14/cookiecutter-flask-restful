from time import time
import logging
from flask import request
from base.utils import get_client_ip

request_logger = logging.getLogger("api.request")


def register_middleware(app):
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
