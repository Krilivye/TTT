.PHONY: run integration check

run:
	firefox index.html

integration:
	python setup.py test

check:
	.tox/py35/bin/pytest

fullcheck:
	.tox/py35/bin/pytest --cov TTT/ -n auto
