"""Contains all the routes for sofia."""

from pathlib import Path
from flask import Blueprint, render_template, abort

from . import utils

views = Blueprint("views", __name__)

course_path = Path(Path(__file__).parent.parent / "courses")


@views.route("/")
def index():
    """Return the page"s index."""
    courses = []

    for entry in course_path.glob("*"):
        if entry.is_dir():
            lesson_path = Path(entry / "course.json")

            if lesson_path.exists():
                course_info = utils.load_json(lesson_path)
                course_info["location"] = entry.name

                courses.append(course_info)
            # Skip if the lesson path starts with `.`
            elif not entry.name.startswith("."):
                print(
                    f"Lesson {entry.name} has no `course.json` file. Skipped."
                )

    return render_template("index.html", courses=courses)


@views.route("/course/<string:course_name>/")
def course_(course_name):
    """Returns the lessons inside a course."""

    lessons = []

    lessons_path = Path(course_path / course_name)

    if not lessons_path.exists():
        return abort(404)

    for entry in lessons_path.glob("*"):
        if entry.is_dir():
            if Path(entry / "lesson.json").exists():
                lesson_info = utils.load_json(entry / "lesson.json")
                lessons.append((entry.name, lesson_info))
        elif entry.name.endswith(".md"):
            lessons.append((entry.name, utils.get_headers(entry)[0]))

    course_info = utils.load_json(lessons_path / "course.json")

    return render_template("lessons.html", course=course_info, lessons=lessons)


@views.route("/course/<string:course_name>/<string:lesson_name>")
def lesson_(course_name, lesson_name):
    """Render a lesson."""
    lesson_path = Path(course_path / course_name / lesson_name)

    if not lesson_path.exists():
        return abort(404)

    css_link = '<link rel="stylesheet" href="/static/css/style.css">'

    if lesson_path.is_dir():
        text = ""
        for i, entry in enumerate(lesson_path.glob("*.md")):
            with open(entry, "r", encoding="utf-8") as f:
                text += "" if i == 0 else "<hr>"
                text += f.read()

        lesson_info = utils.load_json(lesson_path / "lesson.json")

        return utils.render_markdown(text, css_link, headers=lesson_info)

    with open(lesson_path, "r", encoding="utf-8") as f:
        if lesson_path.name.endswith(".md"):

            headers, i = utils.get_headers(lesson_path)

            text = "\n".join(f.readlines()[i:])

            return utils.render_markdown(text, css_link, headers=headers)
        # Allows for custom files such as css or even html.
        # Obviously this opens up the possibility of malicious
        # Javascript, but it is up to the user to check their files.
        # They are warned in the docs.
        return f.read()
