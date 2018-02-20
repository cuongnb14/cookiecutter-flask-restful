from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.base import *


def register_admin(app):
    admin = Admin(app, name='admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
