install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main main.py test_main.py *.ipynb

format:	
	black *.py 

lint:
#disable comment to test speed
#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
#ruff linting is 10-100X faster than pylint
	ruff check *.py test_*.py --fix

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here

all: install lint test format deploy
