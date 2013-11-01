# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name = 'ijson',
    version = '1.1',
    author = 'Ivan Sagalaev',
    author_email = 'maniac@softwaremaniacs.org',
    packages = ['ijson', 'ijson.backends'],
    platforms = ('Any'),
    install_requires = ['setuptools'],
    zip_safe = False,
    url = 'https://github.com/isagalaev/ijson',
    license = 'LICENSE.txt',
    description = 'Iterative JSON parser with a standard Python iterator interface',
    long_description = open('README.rst').read(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
