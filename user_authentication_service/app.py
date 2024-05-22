#!/usr/bin/env python3
"""
Route module
"""


from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)