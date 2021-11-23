"""sofia, a tool for learning via simple lessons. Licensed under GPL v3.0"""

from flask import Flask

app = Flask(__name__)

# pylint: disable=wrong-import-position
from app import views
