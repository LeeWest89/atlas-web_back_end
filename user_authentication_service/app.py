#!/usr/bin/env python3
"""
Route module
"""


from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def message():
    """return a JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Returns jsonified email and message or a VauleError message"""
    email = request.form.get("email")
    pswd = request.form.get("password")

    try:
        user = AUTH.register_user(email, pswd)

        return (jsonify({"email": user.email, "message": "user created"}), 200)

    except ValueError:
        return (jsonify({"message": "email already registered"}), 400)


@app.route('/sessions', methods=['POST'])
def login():
    """Creates a cookie with the session_id as key"""
    email = request.form.get("email")
    pswd = request.form.get("password")

    if not email or not pswd:
        abort(400)

    if not AUTH.valid_login(email, pswd):
        abort(401)

    s_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", s_id)

    return (response)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logs user out"""
    s_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(s_id)

    if user:
        AUTH.destroy_session(user.id)
        return (redirect("/"))

    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
