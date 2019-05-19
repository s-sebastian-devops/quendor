all: format lint

format:
	black .

lint:
	flake8 --statistics .

run:
	python3 -m quendor $(story)

clean:
	rm -f quendor.py
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
