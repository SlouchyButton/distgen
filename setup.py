from setuptools import setup

from setuptools.command.build_py import build_py
from setuptools.command.install import install

try:
    from build_manpages.build_manpages import build_manpages
    from build_manpages import get_build_py_cmd
    from build_manpages import get_install_cmd
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