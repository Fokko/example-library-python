
test:
	cd /app && pip install --user .[test] && pytest

build:
	cd /app && python setup.py bdist_wheel

upload:
  echo "[server-login]" > ~/.pypirc
  echo "repository=https://upload.pypi.org/legacy/" >> ~/.pypirc
  echo "username=" ${PYPI_USER} >> ~/.pypirc
  echo "password=" ${PYPI_PASSWORD} >> ~/.pypirc
	twine upload dist/*
