#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'selenium'
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(hwine): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='github_selenium',
    version='0.1.1',
    description="Helper for 2FA login to GitHub",
    long_description=readme + '\n\n' + history,
    author="Hal Wine",
    author_email='hwine@mozilla.com',
    url='https://github.com/hwine/github_selenium',
    packages=find_packages(include=['github_selenium']),
    include_package_data=True,
    install_requires=requirements,
    license="MPL 2.0 license",
    zip_safe=False,
    keywords='github_selenium',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
