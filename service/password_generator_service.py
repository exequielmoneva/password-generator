import random
import string

from flask_restful import reqparse


class PassGenerator:
    @staticmethod
    def generate(user, length):
        password = ''.join(
            [random.choice(
                string.ascii_uppercase
                + string.digits + string.ascii_lowercase +
                string.punctuation
            ) for i in range(length)
            ]
        )
        return password

    @staticmethod
    def parser():
        parser = reqparse.RequestParser()
        parser.add_argument("user")
        parser.add_argument("length")
        args = parser.parse_args()
        user = args["user"]
        length = int(args["length"])
        return user, length
