#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask
from flask.globals import request
from flask.json import jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def welcome():
    """
    / GET endpoint.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    /users POST end-point
    """
    email = request.form['email']
    passw = request.form['password']
    try:
        user = AUTH.register_user(email, passw)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
