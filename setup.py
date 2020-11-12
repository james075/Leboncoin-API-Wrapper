from setuptools import setup

setup(
    name='leboncoin-api-wrapper',
    version='0.1',
    license='MIT',
    install_requires=[
        'requests >= 2.25.0',
        'cloudscraper >= 1.2.48',
        'pydantic >= 1.7.2',
    ],
    packages=['leboncoin_api_wrapper'],
)
