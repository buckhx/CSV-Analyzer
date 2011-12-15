#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup
setup(
    name='csv_analyzer',
    version='0.1.2',
    description='Simple, quick, structed data analysis',
    author='Buck Heroux',
    author_email='buck@nextbigsound.com',
    url='https://github.com/buckheroux/CSV-Analyzer',
    scripts=['bin/csv'],
    packages=['csv_analyzer','csv_analyzer.strategies','csv_analyzer.masks'])
