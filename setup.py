#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor vips engine
# https://github.com/thumbor/thumbor-vips-engine

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

from distutils.core import setup

try:
    from thumbor_vips_engine import __version__
except ImportError:
    __version__ = "0.0.0"

TESTS_REQUIREMENTS = [
    "coverage==5.*,>=5.0.3",
    "flake8==3.*,>=3.7.9",
    "isort==4.*,>=4.3.21",
    "preggy==1.*,>=1.4.4",
    "pylint==2.*,>=2.4.4",
    "pytest==5.*,>=5.3.5",
    "pytest-asyncio==0.*,>=0.10.0",
    "pytest-cov==2.*,>=2.8.1",
    "pytest-tldr==0.*,>=0.2.1",
    "pytest-xdist==1.*,>=1.31.0",
    "pytest-approvaltests>=0.2.3,<1.0.0",
    "pytest-sugar>=0.9.4,<1.0.0",
    "pytest-icdiff>=0.5,<1.0.0",
    "approvaltests>=3.1.0,!=3.1.1",
    "yanc==0.*,>=0.3.3",
    "mock==3.*,>=3.0.5",
    "pyssim==0.*,>=0.4.0",
]


setup(
    name="thumbor_vips_engine",
    version=__version__,
    description="thumbor libvips engine",
    long_description="""
thumbor engine using the libvips imaging library for transforming images
""",
    keywords=("imaging face detection feature thumbnail libvips vips"),
    author="Bernardo Heynemann",
    author_email="heynemann@gmail.com",
    url="https://github.com/thumbor/thumbor_vips_engine",
    license="Apache2",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    packages=["thumbor_vips_engine"],
    package_dir={"thumbor_vips_engine": "thumbor_vips_engine"},
    include_package_data=True,
    package_data={"": ["*.xml"]},
    install_requires=[
        "thumbor>=7.0.0b1",
        "pycurl>=7.44.1,<8.0.0",
        "pyvips>=2.1.16,<3.0.0",
    ],
    extras_require={"tests": TESTS_REQUIREMENTS},
    entry_points={
        "console_scripts": [],
    },
)
