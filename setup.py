# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='qgen',
    version='1.3',
    description='Question generating framework',
    long_description="Generate a random value of questions based on a template",
    author='Javon Davis, Howard Edwards, Alexander Nicholson',
    author_email='javonldavis14@gmail.com, howarde.jr@hotmail.com, alexj.nich@hotmail.com',
    url='https://github.com/JA-VON/QGenPY',
    license="MIT",
    packages=find_packages(exclude=('tests', 'docs'))
)
