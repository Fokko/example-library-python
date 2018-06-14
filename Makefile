
test:
	cd /root && pip install --user .[test] && pytest

build:
	cd /root && python setup.py bdist_wheel

upload:
	export DATABRICKS_TOKEN
	export DATABRICKS_HOST
	if [ -f "~/.databrickscfg" ]
	then
	  echo "Using supplied configuration"
	else
	  echo -en "${DATABRICKS_HOST}\n${DATABRICKS_TOKEN}" | databricks configure --token
	fi
	set -x
	databricks fs ls
