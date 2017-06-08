#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Country-Template',
    version='1.2.3',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description=u'OpenFisca tax and benefit system for Country-Template',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/openfisca-country-template',
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 14.0.0, < 15.0',
        ],
    extras_require = {
        'api': [
            'OpenFisca-Web-API >= 4.0.0, < 6.0',
            ],
        'test': [
            'flake8',
            'flake8-print',
            'nose',
            ]
        },
    packages=find_packages(),
    test_suite='nose.collector',
    )
