from flask import Flask, request, jsonify

from service.password_generator_service import PassGenerator

app = Flask(__name__)


class PasswordGenerator:
    @app.route("/generate", methods=["POST"])
    def generate():
        if request.method == 'POST':
            user, length = PassGenerator.parser()
            password = PassGenerator.generate(user, length)
            # TODO
            # Validate if the user exists so you can assign new pass
            # Store the user with the pass and return an id
            return jsonify("Your new password is: {} ".format(password)), 200

    @app.route('/<id_>/auth')
    def get(id_):
        return "in progress"
        """#TODO
        # Validate against DB and check if user exists
        # If user exists, return user and password
        # Return new password and id from DB
        # If it doesn't, return NOT FOUND and a personalised message"""


if __name__ == '__main__':
    app.run()
