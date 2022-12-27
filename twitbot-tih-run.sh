#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
readonly SCRIPT_DIR
# shellcheck source=/dev/null
. "${SCRIPT_DIR}/venv"
python "${SCRIPT_DIR}/today_in_history_bot.py"
