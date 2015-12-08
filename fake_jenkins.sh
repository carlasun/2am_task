#!/bin/bash
VE=venv
if [ -d ${VE} ] ; then
  rm -rf ${VE}
fi

virtualenv ${VE} --no-site-packages

. ${VE}/bin/activate

pip install -r test-requirements.txt
py.test test/test_23andme_task.py

deactivate
