#!/bin/sh

. ./setup.sh
alacritty --working-directory `pwd` --command bash --rcfile "scripts/startrc.sh" -i  &

if [ -n "$1" ]; then
    nvim "day$1.py"
else
    nvim .
fi
