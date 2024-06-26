#!/usr/bin/env python3
"""
Route module
"""


from flask import Flask, jsonify, request, abort, redirect
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
def logout() -> str:
    """Logs user out"""
    s_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(s_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/', code=302)

    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Returns jsonified email and code 200 or abort 403"""
    s_id = request.cookies.get('session_id')

    if s_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(s_id)

    if user:
        return (jsonify({'email': user.email}), 200)

    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Creates reset token for passwords"""
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)

        if not reset_token:
            abort(403)

        return (jsonify({"email": email, "reset_token": reset_token}), 200)

    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Updates password"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)

    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
