#!/bin/bash

set -e

if [[ -z $VIRTUAL_ENV ]]; then
    virtualenv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade -r requirements.txt -r requirements-dev.txt -e .
python setup.py develop
python setup.py test
python setup.py flake8
yapf -r -i jupyter_utils
python setup.py sdist bdist bdist_wheel
