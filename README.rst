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
* Source: https://github.com/Stibbons/jupyter_utils

Usage
-----

Install `jupyter_utils` in Anaconda:

.. code-block:: bash

    $ source activate my_conda_env
    $ pip install jupyter_utils

From now, on every Jupyter notebook that use this conda environment, you can
install any missing anaconda package directly from the cell:

.. code-block:: python

    from jupyter_utils import conda
    conda.install("numpy")


Note: only dependencies described in `requirements.txt` will be installed when
using `pip install`. The development dependencies (pylint,...) and **not**
installed on deployment.

Contributing
------------

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
