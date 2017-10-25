from flask_restful import Resource
from flask_restful import reqparse
from models.base import User

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='{error_msg}')
user_parser.add_argument('email', type=str, required=True, help='{error_msg}')

delete_user_parser = reqparse.RequestParser()
delete_user_parser.add_argument('user_id', type=str, required=True, help='{error_msg}')


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        users = list(user.as_dict() for user in users)
        return {"status": "OK", "message": users}

    def post(self):
        args = user_parser.parse_args()
        return {"status": "OK", "message": str(args)}

    def delete(self):
        args = user_parser.parse_args()
        return {"status": "OK", "message": args}
