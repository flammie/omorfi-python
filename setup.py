#!/usr/bin/env python3
"""Python setup for some pypi stuff?"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omorfi",
    version="0.10.0",
    author="Flammie A Pirinen",
    author_email="flammie@iki.fi",
    description="Open morphology for Finnish, python bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flammie/omorfi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords="finnish nlp morphology",
    python_requires=">=3.5",
    install_requires=["pyhfst"],
)
