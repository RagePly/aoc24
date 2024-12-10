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
imported: 10 solution(s) in 1179 μs
running: all with benchmark
day1.part1: ~ (632 μs 15809 samples)
day1.part2: ~ (19 ms 535 samples)
day2.part1: ~ (1236 μs 8089 samples)
day2.part2: ~ (5057 μs 1978 samples)
day3.part1: ~ (276 μs 36240 samples)
day3.part2: ~ (398 μs 25080 samples)
day4.part1: ~ (15 ms 677 samples)
day4.part2: ~ (19 ms 531 samples)
day5.part1: ~ (2040 μs 4902 samples)
day5.part2: ~ (1535 μs 6515 samples)
day6.part1: ~ (2725 μs 3670 samples)
day6.part2: ~ (3331 ms 4 samples)
day7.part1: ~ (4260 μs 2348 samples)
day7.part2: ~ (7258 μs 1378 samples)
day8.part1: ~ (405 μs 24656 samples)
day8.part2: ~ (938 μs 10658 samples)
day9.part1: ~ (7767 μs 1288 samples)
day9.part2: ~ (1600 ms 7 samples)
day10.part1: ~ (12 ms 858 samples)
day10.part2: ~ (12 ms 853 samples)
total: 5041 ms
```

## Environment

Description of my setup and how I use it.

* I use `setup.sh` for activating and configuring the python virtual environment.
* I usually have two terminals open, one for editing in NeoVim and one for running scripts/solutions. `start.sh` will create the terminal windows and setup the virtual environment in both.
* When each day's challenge is released I run `today.py` wich will download the input into `input/day{nr}.txt`. Any example inputs that I want to use I manually put under `input/day{nr}.{example nr}.txt`.
* `aoc.py` is a *runner* which will by default run functions `part1` and `part2` in `day{nr}.py` on the corresponding tests and input. `run.sh` will run this *runner* at any time when a solution is updated.
* To benchmark, `aoc.py --all --bench --hide --no-test` will hide the answers and only output the measured time for running each part on the corresponding input.
