all: format lint

format:
	black .

lint:
	flake8 --statistics .

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
