#!/usr/bin/env python3
""" Basic flask app """

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect, Response


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def basic():
    """ Basic app """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ function that register an User """
    data = dict(request.form)
    email = data.get('email')
    password = data.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ function that creater a user login """
    data = dict(request.form)
    email = data.get('email')
    password = data.get('password')

    if (AUTH.valid_login(email, password)):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> Response:
    """method that logout session """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ function profile user """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if (user):
        return jsonify({"email": f"{user.email}"}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ method that get password token """
    email = request.form.get('email')
    try:
        user = AUTH._db.find_user_by(email=email)
        token = AUTH.get_reset_password_token(user.email)
        return jsonify({"email": f"{email}", "reset_token": f"{token}"}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ function that update a password """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_pwd = request.form.get('new_password')

    try:
        user = AUTH._db.find_user_by(email=email)
        AUTH.update_password(reset_token, new_pwd)
        return jsonify(
                {"email": f"{user.email}", "message": "Password updated"}
            ), 200
    except ValueError:
        abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
