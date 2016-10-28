===============================
jupyter_utils
===============================

.. image:: https://travis-ci.org/Stibbons/jupyter_utils.svg?branch=master
    :target: https://travis-ci.org/Stibbons/jupyter_utils
.. image:: https://badge.fury.io/py/jupyter_utils.svg
    :target: https://pypi.python.org/pypi/jupyter_utils/
    :alt: Pypi package

A set of Python utility methods to ease usage of Jupyter notebook

* Free software: MIT
* Documentation: jupyter_utils.readthedocs.org/en/latest/
* Source: https://github.com/Stibbons/jupyter_utils

Features
--------

* TODO

Usage
-----

Create a virtualenv:

.. code-block:: bash

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip  # Force upgrade to latest version of pip

Setup for production:

.. code-block:: bash

    $ pip install -r requirements.txt .

Setup for development and unit tests

.. code-block:: bash

    $ pip install -r requirements.txt -r requirements-dev.txt -e .

Build source package:

.. code-block:: bash

    python setup.py sdist

Build binary package:

.. code-block:: bash

    python setup.py bdist

Build Wheel package:

.. code-block:: bash

    python setup.py bdist_wheel
