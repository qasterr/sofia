# Courses

Sofia is ordered in courses, which contain lessons.
These can be made by you or downloaded from the internet.
Here's a guide on how to do this:

**WARNING: Downloaded courses can serve malicious HTML and JavaScript. Be careful with what you download!**

## Folder structure

To be recognized as a valid course, the course must be located in `./courses`.
It must contain also a `course.json` file to indicate information about the course.

```
courses/
├─ course_name/
│  ├─ course.json
```

### course.json
A `course.json` should have the following keys: `name`, `description`, `icon`, `author`, `version`.

#### Example `course.json` file
```json
{
    "name": "Lorem Ipsum",
    "description": "Dolor sit amet.",
    "icon": "📜",
    "author": "John Doe",
    "version": "1.0.0"
}
```


Obviously courses are useless if they don't have content, this can be done via two ways:

### Single markdown file

The most basic way to make a lesson is by making a markdown file.
To do this, add a `.md` file in the course directory.

```bash
touch 01-single-file.md
```

To be valid they have to have a header with info.
This can be done by adding `---` before the content.
Before that are the headers. These are written in YAML.

To be valid it must contain the following keys:

`name` - The name of the lesson. This will be displayed in the lessons list.

`description` - A short description of the contents of the lesson.

`icon` - An emoji which stands for the lesson.

Optional values:

`css` - An array of links to custom css files. These can be from third-parties or be held into the course directory.
To do so just add the folling entry to the css: `"/courses/<course_name>/style.css"`. More than one css file can be added.

#### Example file

```text
name: Lorem Ipsum
description: Dolor sit amet.
icon: 📜
---
# Lorem Ipsum
Dolor sit amen
```

### Folder

For long lessons, it is better to make a folder whose contents will be merged together.
To do this make a folder in the course directory and add a `lesson.json`
`lesson.json` files should contain the same contents the header but in JSON format.

#### Example `lesson.json` file
```json
{
    "name": "Lorem Ipsum",
    "description": "Dolor sit amet.",
    "icon": "📜"
}
```
This will be the header values for the whole lesson, so **DO NOT PUT HEADERS IN THE MARKDOWN FILES**.

#### Folder architecture

```
courses/
├─ course_name/
│  ├─ 01-lesson/
│  │  ├─ 01-lorem.md
│  │  ├─ 02-ipsum.md
│  │  ├─ lesson.json
```

## Final lesson structure
A complete lesson should look like this:

```
courses/
├─ course_name/
│  ├─ 01-lesson/
│  │  ├─ 01-file.md
│  │  ├─ 02-file.md
│  │  ├─ lesson.json
│  ├─ 02-lesson.md
│  ├─ course.json
```
