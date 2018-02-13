from flask_restful import Resource
from flask_restful import reqparse
from models.base import User
from base.paginator import Paginator
from base.utils import ok, fail
from tasks.celery import add_user
from objects import db

from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)

page_parser = reqparse.RequestParser()
page_parser.add_argument('offset', type=str, required=False, help='{error_msg}')
page_parser.add_argument('limit', type=str, required=False, help='{error_msg}')

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='{error_msg}')
user_parser.add_argument('email', type=str, required=True, help='{error_msg}')

delete_user_parser = reqparse.RequestParser()
delete_user_parser.add_argument('user_id', type=str, required=True, help='{error_msg}')

token_parser = reqparse.RequestParser()
token_parser.add_argument('username', type=str, required=True, help='{error_msg}')
token_parser.add_argument('password', type=str, required=True, help='{error_msg}')


class TokenResource(Resource):
    def post(self):
        parser = token_parser.parse_args()
        username = parser.get("username")
        password = parser.get("password")

        # Fake authenticate
        if username == 'test' and password == 'test':
            access_token = create_access_token(identity=username)
            data = {
                "username": username,
                "password": password,
                "access_token": access_token,
            }
            return ok(data)

        return fail("Authenticate fail", 401)


class UserResource(Resource):
    # TODO: remove it. This is test jwt auth
    @jwt_required
    def get(self):
        users = User.query
        page = page_parser.parse_args()
        limit = page.get("limit")
        offset = page.get("offset")
        paginator = Paginator(users, offset, limit)
        users = list(user.as_dict() for user in users)
        return ok(users, paginator)

    def post(self):
        args = user_parser.parse_args()
        username = args.get("username")
        email = args.get("email")

        # TODO: Sample use celery task
        # Add user by celery task
        add_user.delay(username, email)

        # Or add user like normal
        # user = User(username=username, email=email)
        # db.session.add(user)
        # db.session.commit()
        return {"status": "OK", "message": str(args)}


class UserDetailResource(Resource):
    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"status": "OK", "message": "Deleted user id: " + user_id}
