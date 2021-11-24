requirements:
	pip3 freeze > requirements.txt

black:
	python3 -m black app/**.py run.py -l 79

lint:
	python3 -m pylint -d fixme app/**.py run.py

check: black lint

run:
	python3 run.py