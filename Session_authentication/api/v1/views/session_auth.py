#!/usr/bin/env python3
"""Views for session_auth"""


from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
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

    try:
        users = User.search({'email': email})
        user = users[0]

    except Exception:
        return (jsonify({"error": "no user found for this email"}), 404)

    if not user.is_valid_password(password):
        return (jsonify({"error": "wrong password"}), 401)

    from api.v1.app import auth

    s_name = os.getenv('SESSION_NAME')
    s_id = auth.create_session(user.id)
    response = jsonify(user.to_json())

    response.set_cookie(s_name, s_id)
    return (response)

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout user, destroy session"""
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)

    if destroy_session:
        return (jsonify({}), 200)
    
    abort(404)
