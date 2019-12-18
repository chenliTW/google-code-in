import os
from setuptools import setup

setup(
    name = "tictactoe",
    version = "0.8",
    author = "Chenlitw",
    author_email = "ab0897867564534231@gmail.com",
    description = "old school Tic Tac Toe",
    license = "BSD",
    url = "",
    packages=['tictactoe'],
    entry_points = {
        'console_scripts' : ['tictactoe = tictactoe.game:main']
    },
    data_files = [
        ('share/applications/', ['tictactoe.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
