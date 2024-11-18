#!/bin/bash

echo day*.py | entr -c ./aoc.py $*
