"""sofia, a tool for learning via simple lessons. Licensed under GPL v3.0"""

from flask import Flask
from app.views import views

app = Flask(__name__)
app.register_blueprint(views)
