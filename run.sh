#!/bin/bash

ls day*.py | sed -r 's/ /\n/g' | entr -c ./aoc.py $*
