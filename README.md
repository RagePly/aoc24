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
imported: 15 solution(s) in 1897 μs
running: all with benchmark
day1.part1: ~ (635 μs 15735 samples)
day1.part2: ~ (19 ms 533 samples)
day2.part1: ~ (1281 μs 7807 samples)
day2.part2: ~ (5193 μs 1926 samples)
day3.part1: ~ (279 μs 35873 samples)
day3.part2: ~ (380 μs 26265 samples)
day4.part1: ~ (15 ms 663 samples)
day4.part2: ~ (19 ms 540 samples)
day5.part1: ~ (2078 μs 4813 samples)
day5.part2: ~ (1613 μs 6198 samples)
day6.part1: ~ (2839 μs 3522 samples)
day6.part2: ~ (3483 ms 3 samples)
day7.part1: ~ (4299 μs 2326 samples)
day7.part2: ~ (7550 μs 1325 samples)
day8.part1: ~ (426 μs 23454 samples)
day8.part2: ~ (1004 μs 9956 samples)
day9.part1: ~ (8620 μs 1161 samples)
day9.part2: ~ (1683 ms 6 samples)
day10.part1: ~ (12 ms 820 samples)
day10.part2: ~ (12 ms 807 samples)
day11.part1: ~ (1571 μs 6364 samples)
day11.part2: ~ (59 ms 171 samples)
day12.part1: ~ (23 ms 442 samples)
day12.part2: ~ (29 ms 346 samples)
day13.part1: ~ (6173 ms 2 samples)
day13.part2: ~ (1273 μs 7852 samples)
day14.part1: ~ (24 ms 411 samples)
day14.part2: ~ (80 ns 40252877 samples)
day15.part1: ~ (11 ms 917 samples)
day15.part2: ~ (25 ms 404 samples)
total: 12 s
```

## Environment

Description of my setup and how I use it.

* I use `setup.sh` for activating and configuring the python virtual environment.
* I usually have two terminals open, one for editing in NeoVim and one for running scripts/solutions. `start.sh` will create the terminal windows and setup the virtual environment in both.
* When each day's challenge is released I run `today.py` wich will download the input into `input/day{nr}.txt`. Any example inputs that I want to use I manually put under `input/day{nr}.{example nr}.txt`.
* `aoc.py` is a *runner* which will by default run functions `part1` and `part2` in `day{nr}.py` on the corresponding tests and input. `run.sh` will run this *runner* at any time when a solution is updated.
* To benchmark, `aoc.py --all --bench --hide --no-test` will hide the answers and only output the measured time for running each part on the corresponding input.
