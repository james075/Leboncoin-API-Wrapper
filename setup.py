from setuptools import setup

setup(
    name='leboncoin-api-wrapper',
    url="https://github.com/Shinyhero36/Leboncoin-API-Wrapper",
    version='0.1',
    license='MIT',
    install_requires=[
        'requests >= 2.25.0',
        'cloudscraper >= 1.2.48',
        'dataclasses'  # not included in Python <= 3.7
    ],
    author="Shinyhero36",
    setup_requires=['setuptools_scm'],  # Also include Ressources files
    include_package_data=True,
    packages=['leboncoin_api_wrapper'],
)
