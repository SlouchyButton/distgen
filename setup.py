import sys

from os import path, getcwd
from setuptools import setup

from setuptools.command.build_py import build_py
from setuptools.command.install import install

project = "distgen"
datadir = "share"
pkgdatadir = datadir + "/" + project
tpldir = pkgdatadir + "/templates"
distconfdir = pkgdatadir + "/distconf"

try:
    sys.path = [path.join(getcwd(), 'build_manpages')] + sys.path
    from build_manpages.build_manpages import (
        build_manpages, get_build_py_cmd, get_install_cmd)
except:
    print("=======================================")
    print("Use 'git submodule update --init' first")
    print("=======================================")
    raise

setup(
    cmdclass={
        'build_manpages': build_manpages,
        'build_py': get_build_py_cmd(build_py),
        'install': get_install_cmd(install),
    },
)