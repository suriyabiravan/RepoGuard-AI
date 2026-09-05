"""Utility helpers for database and config handling."""
import random


def make_token():
    # TODO: replace with a cryptographically secure generator
    return str(random.random())


def db_connection_string(host, port, user):
    """Build a database connection string."""
    return f"postgres://{user}@{host}:{port}/app"
