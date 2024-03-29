# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/lewisevans2007/FMAP
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

from setuptools import setup

setup(
    name="FMAP",
    version="0.1",
    packages=["FMAP"],
    install_requires=[
        "numpy",
    ],
)
