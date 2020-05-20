from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/test_db'

db = PyMongo(app).db


@app.errorhandler(404)
def not_found(error=None, msg='The requested URL was not found on the server.'):
    message = {
        'detail': msg
    }

    return jsonify(message), 404


@app.route('/')
def list_users():
    users = db.users.find({}, {'_id': False})

    return jsonify(list(users))


@app.route('/one', methods=['GET', 'DELETE'])
def get_user():
    int_keys = ['location.street.number', 'location.postcode', 'dob.age', 'registered.age']
    params = {k: int(v) if k in int_keys else v for k, v in request.args.items()}
    print(params)

    if request.method == 'GET':
        user = db.users.find_one(params, {'_id': False})

        if user:
            return jsonify(user)
    else:  # DELETE method
        result = db.users.delete_one(params)

        if result.deleted_count == 1:
            return jsonify(), 204

    return not_found(msg='Not found user with provided parameters')


if __name__ == '__main__':
    app.run()
