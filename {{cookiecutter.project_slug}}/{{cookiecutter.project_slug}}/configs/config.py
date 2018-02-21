import os
from datetime import timedelta

env = os.getenv

# SECURITY CONFIGURATION
# ----------------------------------------------------------

# The secret key is needed to keep the client-side sessions secure. Raises exception if FLASK_SECRET_KEY not configured.
SECRET_KEY = env('FLASK_SECRET_KEY')

DEBUG = False

# FLASK RESTful CONFIG
# ----------------------------------------------------------
BUNDLE_ERRORS = True

# MYSQL DATABASE CONFIG
# ----------------------------------------------------------
DB_HOST = env('DB_HOST', '127.0.0.1')
DB_PORT = env('DB_PORT', '3309')
DB_USER = env('DB_USER', 'root')
DB_PASS = env('DB_PASS', '123456')
DB_NAME = env('DB_NAME', '{{cookiecutter.project_slug}}')

SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CELERY CONFIG
# ----------------------------------------------------------
CELERY_BROKER_URL = env('CELERY_BROKER_URL', 'redis://localhost:6378')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', 'redis://localhost:6378')

# Flask-JWT-Extended CONFIG
# ----------------------------------------------------------
# TODO: Change it
JWT_SECRET_KEY = env('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)

# LOGGING CONFIG
# ----------------------------------------------------------
LOGGER_NAME = '{{cookiecutter.project_slug}}'
SLACK_API_KEY = env('SLACK_API_KEY')
LOG_FILE = "logs/api.ERROR.log"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s] """%(message)s"""'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'app-file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs/app.log',
            'maxBytes': 100 * 1024 * 1024,  # 100Mb
            'backupCount': 3,
        },
        'request-file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs/api.request.log',
            'when': 'D',
            'backupCount': 3,

        },
        'slack-error': {
            'level': 'ERROR',
            'icon_emoji': ':beetle:',
            'username': 'PF Push notification API Error',
            'api_key': SLACK_API_KEY,
            'class': 'slacker_log_handler.SlackerLogHandler',
            'channel': '#api-error'
        },
    },
    'loggers': {
        'slack.error': {
            'handlers': ['slack-error'],
            'propagate': False,
            'level': 'ERROR',
        },
        'api.request': {
            'handlers': ['request-file', 'slack-error'],
            'propagate': False,
            'level': 'INFO',
        },
        '{{cookiecutter.project_slug}}': {
            'handlers': ['app-file', 'console'],
            'propagate': False,
            'level': 'INFO',
        },
    }
}

# OTHER CONFIG HERE
# ----------------------------------------------------------
