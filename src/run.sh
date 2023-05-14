#!/bin/bash

# Virtual environment is created for the quiz
python3 -m venv quiz-venv
# Activate the virtual environment
source quiz-venv/bin/activate
# Installs all packages that are need from requirements.txt
pip3 install -r requrirements.txt
# Clears the terminal screen for you
clear
# runs the main.py to start the quiz
python3 main.py