#!/usr/bin/env bash

realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

SCRIPT_FULL_PATH=$(realpath "$0")
BIN_DIR=$(dirname "$SCRIPT_FULL_PATH")
ROOT_DIR=$(dirname "$BIN_DIR")

VENV_PATH=$ROOT_DIR/.venv

# Setup environment variables
set -a
source $ROOT_DIR/.env
set +a

# Run script inside venv
source $VENV_PATH/bin/activate
python $ROOT_DIR/main.py
deactivate