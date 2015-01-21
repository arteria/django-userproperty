#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_userproperty

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_userproperty.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.md').read()
#history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='Django-UserProperty',
    version=version,
    packages=['django_userproperty', ],
    license='BSD',
    description='django Userproperty',
    ong_description=readme,  # + '\n\n' + history,
    install_requires=open('requirements.txt').read().split('\n'),
    author='arteria GmbH',
    author_email='admin@arteria.ch',
)
