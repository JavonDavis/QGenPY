# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='qgen',
    version='0.0.1',
    description='Question generating language',
    long_description=readme,
    author='Javon Davis, Howard Edwards, Alexander Nicholson',
    author_email='javonldavis14@gmail.com',  # TODO - add the other contributor emails
    url='',  # TODO - add repository url
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
