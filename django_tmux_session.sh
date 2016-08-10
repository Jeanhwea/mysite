#!/bin/bash

tmux new-session -d -n DjangoSession './manage.py shell'
tmux split-window -h
tmux select-pane -L
tmux split-window -v './manage.py runserver'
tmux select-pane -R
tmux -2 attach-session -d
