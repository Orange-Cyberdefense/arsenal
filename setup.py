#!/usr/bin/env python3
"""
Packaging setup for Arsenal
"""
from pathlib import Path
from setuptools import find_packages, setup

import arsenal as package


def read_file(filename):
    """Get the contents of a file"""
    with open(Path(__file__).resolve().parent / filename) as file:
        return file.read()


setup(
    name=package.name,
    version=package.__version__,
    packages=find_packages(),
    install_requires=read_file('requirements.txt'),
    include_package_data=True,
    url=package.__url__,
    license=package.__license__,
    author=package.__author__,
    author_email=package.__author_email__,
    description=package.__doc__.strip(),
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords=[
        'security',
        'pen testing',
        'cli',
        'tools',
        'tmux',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'arsenal = arsenal.app:main',
        ],
    },
)
