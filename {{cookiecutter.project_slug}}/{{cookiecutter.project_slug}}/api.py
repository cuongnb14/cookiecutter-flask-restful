from flask import Blueprint
from flask_restful import Api
from resources.user import UserResource, UserDetailResource

api_bp = Blueprint('api', __name__, url_prefix='/v1')
api = Api(api_bp)

# Routers
api.add_resource(UserResource, '/users')
api.add_resource(UserDetailResource, '/users/<int:user_id>')


def register_api(app):
    app.register_blueprint(api_bp)
