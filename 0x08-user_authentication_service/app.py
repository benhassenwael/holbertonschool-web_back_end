#!/usr/bin/env python3
"""Flask app
"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
app = Flask(__name__)

AUTH = Auth()


@app.route('/')
def index():
    """Index route
    """
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'])
def register():
    """Register a new user
    """
    email: str = request.form['email']
    password: str = request.form['password']

    try:
        AUTH.register_user(email, password)
        return jsonify(email=email, message="user created")
    except ValueError:
        return jsonify(message="email already registered"), 400


@app.route('/sessions', methods=['POST'])
def login():
    """User login
    """
    email: str = request.form['email']
    password: str = request.form['password']

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id: str = AUTH.create_session(email)
    resp = jsonify(email='{}'.format(email), message='logged in')
    resp.set_cookie('session_id', session_id)
    return resp


@app.route('/sessions', methods=['DELETE'])
def logout():
    """User logout
    """
    session_id: str = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect('/', code=403)


@app.route('/profile')
def profile():
    """Get user email
    """
    session_id: str = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    return jsonify(email=user.email)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Get reset password token
    """
    email: str = request.form['email']
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify(email=email, reset_token=reset_token)
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Update user password
    """
    email: str = request.form['email']
    reset_token: str = request.form['reset_token']
    new_password: str = request.form['new_password']

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify(email=email, message="Password updated")
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
