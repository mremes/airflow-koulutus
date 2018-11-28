#!/bin/bash

set -ex

source ./environment

# This must be set so that `apache-airflow` package installs
export SLUGIFY_USES_TEXT_UNIDECODE=yes

# Install pipenv if not installed
pip install --user pipenv

# Install dependencies to pipenv
pipenv shell
pipenv install

# Init Airflow metadatabase
airflow initdb
