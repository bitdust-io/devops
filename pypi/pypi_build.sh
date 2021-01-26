#!/bin/bash

curpath=`pwd`

rm -rf dist
mkdir dist
mkdir dist/bitdust

cd ../bitdust/
sourcepath=`pwd`

git checkout-index -a -f --prefix="$curpath/dist/bitdust/"

cd "$curpath/dist/bitdust"
rm -rf release/
rm -rf screenshots/
rm -rf scripts/
rm -rf deploy/
rm -rf dht/entangled_orig/
rm -rf devops/
rm -rf tests/dht/
rm -rf tests/e2e/
rm -rf tests/experiments/
rm .travis.yml
rm setup.py
rm setup_gen.py

mv README.md ..
mv LICENSE.txt ..
mv README.txt ..
mv requirements.txt ..

cd "$curpath/dist/"

cp "$curpath/pypi/setup_gen.py" .

../venv/bin/python3 setup_gen.py

../venv/bin/python3 setup.py sdist bdist_wheel

../venv/bin/python3 -m twine upload dist/*

cd "$curpath"
