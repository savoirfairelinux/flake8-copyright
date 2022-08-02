# -=- encoding: utf-8 -=-
#
# Copyright (C) 2016 Savoir-faire Linux Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import unicode_literals

from setuptools import setup


def get_version(fname='flake8_copyright.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-copyright',
    version=get_version(),
    description='Adds copyright checks to flake8',
    long_description=get_long_description(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    author='Virgil Dupras',
    author_email='virgil.dupras@savoirfairelinux.com',
    url='https://github.com/savoirfairelinux/flake8-copyright',
    keywords='pep8 flake8 copyright',
    py_modules=['flake8_copyright'],
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'flake8.extension': ['C801 = flake8_copyright:CopyrightChecker'],
    },
)
