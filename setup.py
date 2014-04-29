#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import run_to_pdb

setup(

    name = 'call_seq',
    version = '0.0.1',
    description = 'When exception happen, run to pdb.',
    long_description = open('README.md').read(),

    author = 'ya790206',
    url = 'https://github.com/ya790206/run_to_pdb',
    license = 'Apache License Version 2.0',
    platforms = 'any',
    classifiers = [
    ],

    packages = find_packages(),

    entry_points = {
    }

)
