#!/usr/bin/env python3
"""Views for session_auth"""


from flask import jsonify, request, abort, make_response
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Uses session auth for user logins"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return (jsonify({"error": "email missing"}), 400)

    if not password:
        return (jsonify({"error": "password missing"}), 400)

    users = User.search({'email': email})

    if not users:
        return (jsonify({"error": "no user found for this email"}), 404)

    user = users[0]
    if not user.is_valid_password(password):
        return (jsonify({"error": "wrong password"}), 401)

    session = os.getenv('SESSION_NAME')
    response = make_response(jsonify(user.to_json()))

    response.set_cookie(session, auth.create_session(user.id))
    return (response)
