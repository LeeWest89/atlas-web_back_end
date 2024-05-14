#!/usr/bin/env python3
"""Encrypting Passwords"""


import bcrypt


def hash_password(password: str) -> bytes:
    """encodes pasword using bcrypt"""
    pswd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return (pswd)
