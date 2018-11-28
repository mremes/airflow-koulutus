#!/bin/bash

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

apt-get install python-pip python-dev build-essential libssl-dev 
apt-get install make libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev

pyenv install 3.5.2
pyenv local 3.5.2

pip install --user pipenv

