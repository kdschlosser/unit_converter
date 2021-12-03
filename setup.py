import setuptools

from unit_converter.__about__ import (
    __package_name__,
    __license__,
    __version__,
    __author__,
    __author_email__,
    __description__,
    __url__
)

setuptools.setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    url=__url__,
    license=__license__,
    packages=setuptools.find_packages(),
    long_description=__description__,
    classifiers=['License :: OSI Approved :: MIT License'],
)

