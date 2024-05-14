#!/usr/bin/env python3
"""Encrypting Passwords"""


import bcrypt


def hash_password(password: str) -> bytes:
    """encodes pasword using bcrypt"""
    pswd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return (pswd)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if password and hashed_password are the same"""
    return (bcrypt.checkpw(password.encode('utf-8'), hashed_password))
