#!/usr/bin/env python
"""
setup.py for ghe.

https://git.generalassemb.ly/ga-admin-utils/ghe

python setup.py sdist bdist_wheel
"""

import sys

from setuptools import setup, find_packages

VERSION = '0.0.1'

options = dict(
    name='ghe',
    version=VERSION,
    description='GitHub Enterprise CLI Management Tool',
    url='https://git.generalassemb.ly/ga-admin-utils/ghe',
    keywords=['github enterprise', 'ghe'],
    author='Elliott Carlson',
    author_email='elliott.carlson@generalassemb.ly',
    packages=find_packages() + ['ghe'],
    entry_points={'console_scripts': ['ghe = ghe:GHECLI']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
        'Programming Language :: Python'
    ],
    long_description=open('README.rst').read(),
    include_package_data=True
)

setup(**options)