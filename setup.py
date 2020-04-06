#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_pedrolpfbf',
version='0.1',
packages=['dev_aberto'],
scripts=['scripts/hello.py'],
author='Pedro de la Peña Ferreira Bueno Fonseca',
author_email='pedro.d.pena@gmail.com',
install_requires=['requests>=2.23.0']
)