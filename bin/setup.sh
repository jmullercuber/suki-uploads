#!/usr/bin/env bash

realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

SCRIPT_FULL_PATH=$(realpath "$0")
BIN_DIR=$(dirname "$SCRIPT_FULL_PATH")
ROOT_DIR=$(dirname "$BIN_DIR")

VENV_PATH=$ROOT_DIR/.venv

# Create virtual env
python -m venv $VENV_PATH

# Install requirements inside venv
source $VENV_PATH/bin/activate
pip install -r $ROOT_DIR/requirements.txt
deactivate

echo "Setup Complete!"