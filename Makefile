requirements:
	pip3 freeze > requirements.txt

black:
	python3 -m black app/**.py run.py -l 79

lint:
	python3 -m pylint -d fixme app/**.py run.py

check: black lint

docs.serve:
	mkdocs serve

docs.build:
	mkdowcs build

run:
	export FLASK_APP=run.py && \
	export FLASK_ENV=development && \
	flask run