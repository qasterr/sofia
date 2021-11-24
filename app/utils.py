"""Miscelaneous utilities for sofia."""
from typing import Tuple

import re
from pathlib import Path
from json import loads
from markdown import markdown

import yaml


def render_markdown(text: str, *tags: str, headers: dict = None) -> str:
    """Render markdown as HTML.

    Args:
        text (str): The Markdown text.
        *tags (str): Tags to be added to the markdown such as title, css etc.
        headers (dict, optional): A list of headers to search for custom css.
                                  Defaults to None.

    Returns:
        str: [description]
    """

    tags = list(tags)
    text = markdown(text)

    text = text.replace("<html>", "")
    text = text.replace("</html>", "")

    head_text = ""

    if headers is not None:
        if "css" in headers:
            css = headers["css"]

            if isinstance(css, str):
                css = [css]

            for link in css:
                tags.append(f'<link rel="stylesheet" href="{link}">')

        name = "Document"
        if "name" in headers:
            name = headers["name"]

        head_text = " ".join(tags)
        head_text += f"<title>{name}</title>"
        head_text = f"<head>{head_text}</head>"

    return f"<html>{head_text}<body>{text}</body></html>"


def load_json(path: Path) -> dict:
    """Load JSON from a path."""
    with open(path, "r", encoding="utf-8") as f:
        return loads(f.read())


def get_headers(path: Path) -> Tuple[dict, int]:
    """Gets the headers in a sofia .md file. (These are before the first `---`)

    Args:
        path (Path): The path of the file.

    Returns:
        Tuple[dict, int]: The dict contains all the headers and
        the int is after which line the actual documents starts.
    """

    with open(path, "r", encoding="utf-8") as f:
        header_text = re.split("-+", f.read(), 1)[0]

    # Remove the `---` from the text.
    header_text = header_text.split("\n")[:-1]

    i = len(header_text)

    header_text = "\n".join(header_text)

    data = yaml.safe_load(header_text)

    return data, i + 1


# pylint: disable=pointless-string-statement
"""
def render_lesson(path: Path):
    \"""Render a directory as a lesson.\"""
    locations = []

    for entry in path.glob("*"):
        entry_path = Path(path / entry.name)
        if entry.is_dir():
            locations.append((entry_path, "dir"))
        else:
            locations.append((entry_path, "file"))

    lesson_path = Path(path / "lesson.json")
    if lesson_path.exists():
        data = load_json(lesson_path)


    return render_template("lesson.html", locations=locations)
"""
