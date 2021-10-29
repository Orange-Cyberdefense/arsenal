#!/bin/bash
rm -rf dist/*
python3 setup.py check
python3 setup.py sdist
python3 setup.py bdist_wheel --universal
python3 -m twine upload --repository pypi dist/*
