#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from setuptools import setup

# glob._ishidden = lambda x: False

setup(setup_requires=['pytest-runner>=2.0,<3dev'] if 'pytest' in sys.argv or 'test' in sys.argv else [])
