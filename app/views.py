"""Contains all the routes for sofia."""

from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def index():
    """Return the page's index."""
    return render_template("index.html")
