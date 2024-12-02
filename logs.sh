#!/bin/sh
echo '# Logbook AoC 2024'
echo ''
echo 'Notes for each submitted solution, extracted from `git-log`s.'
echo ''
git log --grep='Solution:' --pretty='## %s (`git diff %h`)%n%n%b'
