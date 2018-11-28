#!/bin/bash

set -e

# Go into home folder
cd $AIRFLOW_HOME/..

# Start webserver and scheduler processes
screen -d -m airflow webserver
screen -d -m airflow scheduler
