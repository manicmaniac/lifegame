lifegame
========

An implementation of Conway's game of life in python.

Introduction
------------

Tk-based Conway's game of life.

<img src="data:image/png;base64,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">screenshot</img>

How to play
------------

Make sure to install 'python-tk' package. Then run:

    python lifegame/gui.py

