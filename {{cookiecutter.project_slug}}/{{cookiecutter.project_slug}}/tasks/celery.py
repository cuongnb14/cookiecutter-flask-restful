from celery import Celery
from functools import wraps
from logging.config import dictConfig
from celery.utils.log import get_task_logger
from configs import config

dictConfig(config.LOGGING)

slack_error_logger = get_task_logger("slack.error")

celery = Celery("{{cookiecutter.project_slug}}", backend=config.CELERY_RESULT_BACKEND, broker=config.CELERY_BROKER_URL)


def unexpected_error(func):
    """Decorator to except rest Exceptions of function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            slack_error_logger.exception(e)

    return wrapper


@celery.task(rate_limit="50/m")
@unexpected_error
def send_message(content, device_ids=None, platforms=None, silent=False, data=None):
    """Example long task"""
    slack_error_logger.send_message(content=content, device_ids=device_ids, platforms=platforms, silent=silent, data=data)


@celery.task()
def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
