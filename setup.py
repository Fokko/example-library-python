from setuptools import setup, find_packages

tests_require = [
    'pyspark',
    'pytest',
    'twine'
]

setup(
    name='godatadriven-helpers',
    version='0.1',
    install_requires=[
        'geopy'
    ],
    tests_require=tests_require,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha'
    ],
    extras_require={
        'test': tests_require
    },
    packages=find_packages(exclude=['tests*']),
    include_package_data=True
)
