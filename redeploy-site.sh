#!/bin/bash

cd ~/pe-portfolio

tmux kill-session -t pe-portfolio

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s pe-portfolio 'cd ~/pe-portfolio; source python3-virtualenv/bin/activate; flask run --host=0.0.0.0'
