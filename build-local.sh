#!/bin/bash

echo "1) Cleaning"
rm -fr ./build
rm -fr ./dist
rm -fr ./*.egg-info

echo "2) Building"
python3 -m build

echo "3) Publishing"
python3 -m twine upload --repository testpypi dist/*