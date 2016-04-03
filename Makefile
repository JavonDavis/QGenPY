init:
	pip install -r requirements.txt

test:
	python -m unittest discover -p '*tests.py' -v

