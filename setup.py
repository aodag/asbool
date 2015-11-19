from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)
__version__ = '0.1'
__author__ = 'Atsushi Odagiri'
__author_email__ = 'aodagx@gmail.com'


requires = [
    "six",
]

tests_require = [
    "pytest",
    "pytest-cov",
    "testfixtures",
]


def _read(name):
    try:
        with open(os.path.join(here, name)) as f:
            return f.read()
    except Exception:
        return ''


setup(
    name='asbool',
    packages=find_packages(),
    url='https://github.com/aodag/asbool',
    description='simple converter from ``str`` to ``bool``',
    long_description=_read('README.rst'),
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
