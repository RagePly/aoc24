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
imported: 13 solution(s) in 3784 μs
running: all with benchmark
day1.part1: ~ (646 μs 15478 samples)
day1.part2: ~ (19 ms 539 samples)
day2.part1: ~ (1215 μs 8226 samples)
day2.part2: ~ (4964 μs 2015 samples)
day3.part1: ~ (291 μs 34310 samples)
day3.part2: ~ (398 μs 25116 samples)
day4.part1: ~ (16 ms 634 samples)
day4.part2: ~ (20 ms 508 samples)
day5.part1: ~ (2159 μs 4631 samples)
day5.part2: ~ (1628 μs 6143 samples)
day6.part1: ~ (2839 μs 3523 samples)
day6.part2: ~ (3511 ms 3 samples)
day7.part1: ~ (4247 μs 2355 samples)
day7.part2: ~ (7519 μs 1330 samples)
day8.part1: ~ (422 μs 23680 samples)
day8.part2: ~ (980 μs 10203 samples)
day9.part1: ~ (8040 μs 1244 samples)
day9.part2: ~ (1701 ms 6 samples)
day10.part1: ~ (12 ms 835 samples)
day10.part2: ~ (12 ms 821 samples)
day11.part1: ~ (1579 μs 6332 samples)
day11.part2: ~ (60 ms 167 samples)
day12.part1: ~ (24 ms 424 samples)
day12.part2: ~ (30 ms 335 samples)
day13.part1: ~ (6449 ms 2 samples)
day13.part2: ~ (1337 μs 7478 samples)
total: 12 s
```

## Environment

Description of my setup and how I use it.

* I use `setup.sh` for activating and configuring the python virtual environment.
* I usually have two terminals open, one for editing in NeoVim and one for running scripts/solutions. `start.sh` will create the terminal windows and setup the virtual environment in both.
* When each day's challenge is released I run `today.py` wich will download the input into `input/day{nr}.txt`. Any example inputs that I want to use I manually put under `input/day{nr}.{example nr}.txt`.
* `aoc.py` is a *runner* which will by default run functions `part1` and `part2` in `day{nr}.py` on the corresponding tests and input. `run.sh` will run this *runner* at any time when a solution is updated.
* To benchmark, `aoc.py --all --bench --hide --no-test` will hide the answers and only output the measured time for running each part on the corresponding input.
