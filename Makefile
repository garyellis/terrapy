install:
	python -m virtualenv --python python2.7 venv
	. venv/bin/activate && python setup.py develop

test:
	. venv/bin/activate && pytest tests -v -s --log-cli-level info

clean:
	rm -rf .tox venv *egg.info pip-selfcheck.json
