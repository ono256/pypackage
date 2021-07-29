# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pypackage',
    version='1.2',
    description='basic directory structure',
    author='ono',
    author_email='develop.ono@gmail.com',
    url='https://github.com/ono256/pypackage',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        pypackage = pypackage.cli:execute
    ''',
    install_requires=open('requirements.txt').read().splitlines(),
)
