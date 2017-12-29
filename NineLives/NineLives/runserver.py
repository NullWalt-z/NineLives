"""
This script runs the NineLives application using a development server.
"""

from os import environ
from NineLives import app
from NineLives import Database
from NineLives import views
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
