.PHONY: run integration check fullcheck ulticheck env

run:
	firefox index.html

integration:
	python setup.py test

check:
	.tox/py35/bin/pytest

fullcheck:
	.tox/py35/bin/pytest --cov TTT/ -n auto

ulticheck:
	.tox/py35/bin/pytest --cov TTT/ -n auto --flake8
