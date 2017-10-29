from flask import Blueprint
from flask_restful import Api
from resources.user import UserResource

api_bp = Blueprint('api', __name__, url_prefix='/v1')
api = Api(api_bp)

# Routers
api.add_resource(UserResource, '/users')