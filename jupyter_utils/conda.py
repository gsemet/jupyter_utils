# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess


def install(conda_package_list, channel=None, verbose=True):
    '''
    Install an Anaconda package if your current Jupyter Notebook.

    Parameters
    ----------

    conda_package_list: list of package to install, or single package name.
        Each item in this list should specify an Anaconda package name
        with optionaly its version.

        Example:
            import jupyter_utils
            jupyter_utils.conda.install("numpy")
            jupyter_utils.conda.install(["numpy==1.11", "pandas"])

    channel: additional conda channel to use

    verbose: print output status
    '''
    if not isinstance(conda_package_list, list):
        conda_package_list = [conda_package_list]
    kernel_name = os.environ['CONDA_DEFAULT_ENV'].rpartition("/")[2]

    out = subprocess.check_output("conda install -n {}{}-y {}"
                                  .format(kernel_name,
                                          " " if not channel else " -c {} ".format(channel),
                                          " ".join(conda_package_list))
                                  .split(" ")).decode("utf-8")
    if verbose:
        print("{!s}".format(out))
