import os
from setuptools import setup

setup(
    name = "cfscrapper",
    version = "0.6",
    author = "Chenlitw",
    author_email = "ab0897867564534231@gmail.com",
    description = "codeforce scrapper",
    license = "BSD",
    url = "",
    packages=['cfscrapper'],
    entry_points = {
        'console_scripts' : ['cfscrapper = cfscrapper.cfscrapper:main']
    },
    data_files = [
        ('share/applications/', ['cfscrapper.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)

