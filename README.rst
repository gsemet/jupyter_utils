======================
Jupyter Notebook Utils
======================

.. image:: https://travis-ci.org/Stibbons/jupyter_utils.svg?branch=master
    :target: https://travis-ci.org/Stibbons/jupyter_utils
.. image:: https://badge.fury.io/py/jupyter_utils.svg
    :target: https://pypi.python.org/pypi/jupyter_utils/
    :alt: Pypi package

A set of Python utility methods to ease usage of Jupyter notebook

* Free software: MIT
* Source: https://github.com/Stibbons/jupyter_utils

Installation
============

Install `jupyter_utils` in Anaconda:

.. code-block:: bash

    $ source activate my_conda_env
    $ pip install jupyter_utils

Note: only dependencies described in `requirements.txt` will be installed when using `pip install`.
The development dependencies (pylint,...) and **not** installed on deployment.

Usage
=====

From now, on every Jupyter notebook that use this conda environment, you can install any missing
anaconda package directly from the cell.

Install Anaconda package
------------------------

An anaconda package can be installed directly from the notebook using `! conda install ...`, but
you need to specify the name of the kernel. To simply this, Jupyter Utils provides:

.. code-block:: python

    from jupyter_utils import conda
    conda.install("numpy")

Grid Search CV on Apache Spark
------------------------------

.. code-block:: python

    from jupyter_utils.spark import SparkGridSearchCV
    SparkGridSearchCV(sc, model, params)

Contributing
============

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
