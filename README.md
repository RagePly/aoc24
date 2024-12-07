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
imported: 7 solution(s) in 2532 μs
running: all with benchmark
day1.part1: ~ (637 μs 15686 samples)
day1.part2: ~ (19 ms 537 samples)
day2.part1: ~ (1234 μs 8102 samples)
day2.part2: ~ (4982 μs 2008 samples)
day3.part1: ~ (285 μs 35018 samples)
day3.part2: ~ (391 μs 25530 samples)
day4.part1: ~ (15 ms 681 samples)
day4.part2: ~ (19 ms 529 samples)
day5.part1: ~ (2056 μs 4864 samples)
day5.part2: ~ (1546 μs 6467 samples)
day6.part1: ~ (2704 μs 3698 samples)
day6.part2: ~ (3371 ms 3 samples)
day7.part1: ~ (4124 μs 2425 samples)
day7.part2: ~ (7161 μs 1397 samples)
total: 3448 ms
```

## Environment

Description of my setup and how I use it.

* I use `setup.sh` for activating and configuring the python virtual environment.
* I usually have two terminals open, one for editing in NeoVim and one for running scripts/solutions. `start.sh` will create the terminal windows and setup the virtual environment in both.
* When each day's challenge is released I run `today.py` wich will download the input into `input/day{nr}.txt`. Any example inputs that I want to use I manually put under `input/day{nr}.{example nr}.txt`.
* `aoc.py` is a *runner* which will by default run functions `part1` and `part2` in `day{nr}.py` on the corresponding tests and input. `run.sh` will run this *runner* at any time when a solution is updated.
* To benchmark, `aoc.py --all --bench --hide --no-test` will hide the answers and only output the measured time for running each part on the corresponding input.
