from flask_restful import Resource
from flask_restful import reqparse
from models.base import User
from base.paginator import Paginator
from base.utils import ok
from tasks.celery import add_user

page_parser = reqparse.RequestParser()
page_parser.add_argument('offset', type=str, required=False, help='{error_msg}')
page_parser.add_argument('limit', type=str, required=False, help='{error_msg}')

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='{error_msg}')
user_parser.add_argument('email', type=str, required=True, help='{error_msg}')

delete_user_parser = reqparse.RequestParser()
delete_user_parser.add_argument('user_id', type=str, required=True, help='{error_msg}')


class UserResource(Resource):
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
