"""Contains all the routes for sofia."""

from pathlib import Path
from json import loads
from flask import Blueprint, render_template

views = Blueprint("views", __name__)

courses = Path(Path(__file__).parent.parent / "courses")


@views.route("/")
def index():
    """Return the page"s index."""
    courses = []

    for entry in courses.glob("*"):
        if entry.is_dir():
            lesson_path = Path(entry / "course.json")

            if lesson_path.exists():
                # pylint: disable=invalid-name
                with open(lesson_path, "r", encoding="utf-8") as f:
                    course_info = loads(f.read())

                    course_info["location"] = entry.name

                    courses.append(course_info)
            # Skip if the lesson path starts with `.`
            elif not entry.name.startswith("."):
                print(
                    f"Lesson {entry.name} has no `course.json` file. Skipped."
                )

    return render_template("index.html", courses=courses)
