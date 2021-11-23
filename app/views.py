"""Contains all the routes for sofia."""

from flask import render_template
from app import app


@app.route("/")
def index():
    """Return the page's index."""
    return render_template("index.html")
