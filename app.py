from flask import Flask, request

app = Flask(__name__)


@app.route('/generate')
def post():
    user = request.args.get('user')
    #TODO
    # Validate if the user exists so you can assign new pass
    # Store the user with the pass and return an id
    # Return new password and id from DB

@app.route('/<id_>/password')
def get(id_):
    #TODO
    # Validate against DB and check if user exists
    # If user exists, return user and password
    # If it doesn't, return NOT FOUND and a personalised message



if __name__ == '__main__':
    app.run()
