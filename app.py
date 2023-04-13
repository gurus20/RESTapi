from flask import Flask, jsonify, request
from models import User
from db import Database
import json

app = Flask(__name__)


@app.route('/api/v1/', methods=['GET'])
def home():
    return ({'msg': 'welcome'})


@app.route('/api/v1/users', methods=['GET'])
def get_user():

    user = {
        "username": "gurus207",
        "first_name": "Gurdayal",
        "last_name": "Singh",
        "verified": True
    }

    db = Database()
    db.connect_to_db("users.db")
    db.save_to_db(user)

    return jsonify({})


@app.route('/api/v1/users/create', methods=['POST'])
def create_user():
    if request.method == 'POST':
        if request.data:
            data = json.loads(request.data)
            
            db = Database()
            db.connect_to_db("users.db")
            db.save_to_db(data)

            return jsonify({"msg": "Record Created"})
        else:
            return jsonify({'msg': 'No valid json found in data'})

    return jsonify({})


if __name__ == '__main__':
    app.run()
