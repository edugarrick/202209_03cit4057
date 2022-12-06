#!/bin/bash
# Setup the virtual environment
# to run pytest.py

SCRIPT_PATH=`dirname $0`
SCRIPT_NAME=`basename $0`
REPOSITORY_ROOT=$SCRIPT_PATH/..
VENV_PATH="$REPOSITORY_ROOT/.venv"

# Install Modules
pip install --upgrade pip 
pip install numpy 