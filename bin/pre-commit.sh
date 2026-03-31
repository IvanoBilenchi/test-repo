#!/bin/sh
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests
