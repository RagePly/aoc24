# AoC 24

Repo for 2024 AoC solutions.

## About `today.py`

CLI to download puzzle input.

This script does follow the [automation guidelines](https://www.reddit.com/r/adventofcode/wiki/faqs/automation) on the /r/adventofcode community wiki. Specifically:
- Outbound calls are throttled to every 15 minutes via a timestamp file stored in the user folder `$HOME/.cache/aoc_today_ts`
- Once inputs are downloaded, they are cached locally in `./inputs[/{year}]/day{day}.txt` (the script will never overwrite these files)
  - If you suspect your input is corrupted, you can manually request a fresh copy by deleting both `$HOME/.cache/aoc_today_ts` and `./inputs[/{year}]/day{day}.txt`
- The User-Agent header is set to this repo and my contact info.

## About `setup.sh`

Sets up a correct `venv` and installs all required packages. Will skip the setup and just activate if it already exists.

## Times

```
imported: 14 solution(s) in 3747 μs
running: all with benchmark
day1.part1: ~ (633 μs 15780 samples)
day1.part2: ~ (19 ms 539 samples)
day2.part1: ~ (1233 μs 8107 samples)
day2.part2: ~ (4915 μs 2035 samples)
day3.part1: ~ (286 μs 34982 samples)
day3.part2: ~ (394 μs 25331 samples)
day4.part1: ~ (15 ms 677 samples)
day4.part2: ~ (19 ms 516 samples)
day5.part1: ~ (2157 μs 4636 samples)
day5.part2: ~ (1644 μs 6081 samples)
day6.part1: ~ (2847 μs 3512 samples)
day6.part2: ~ (3527 ms 3 samples)
day7.part1: ~ (4289 μs 2332 samples)
day7.part2: ~ (7524 μs 1329 samples)
day8.part1: ~ (419 μs 23859 samples)
day8.part2: ~ (988 μs 10123 samples)
day9.part1: ~ (7860 μs 1273 samples)
day9.part2: ~ (1717 ms 6 samples)
day10.part1: ~ (12 ms 817 samples)
day10.part2: ~ (12 ms 805 samples)
day11.part1: ~ (1614 μs 6196 samples)
day11.part2: ~ (60 ms 167 samples)
day12.part1: ~ (24 ms 420 samples)
day12.part2: ~ (30 ms 336 samples)
day13.part1: ~ (6542 ms 2 samples)
day13.part2: ~ (1377 μs 7259 samples)
day14.part1: ~ (26 ms 387 samples)
day14.part2: ~ (78 ns 41451218 samples)
total: 12 s
```

## Environment

Description of my setup and how I use it.

* I use `setup.sh` for activating and configuring the python virtual environment.
* I usually have two terminals open, one for editing in NeoVim and one for running scripts/solutions. `start.sh` will create the terminal windows and setup the virtual environment in both.
* When each day's challenge is released I run `today.py` wich will download the input into `input/day{nr}.txt`. Any example inputs that I want to use I manually put under `input/day{nr}.{example nr}.txt`.
* `aoc.py` is a *runner* which will by default run functions `part1` and `part2` in `day{nr}.py` on the corresponding tests and input. `run.sh` will run this *runner* at any time when a solution is updated.
* To benchmark, `aoc.py --all --bench --hide --no-test` will hide the answers and only output the measured time for running each part on the corresponding input.
