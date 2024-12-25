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

Output of running `./aoc.py --all --bench --no-test --hide --no-print`:

```
imported: 25 solution(s) in 2998 μs
running: all with benchmark
day1.part1: ~ (636 μs 15703 samples)
day1.part2: ~ (19 ms 536 samples)
day2.part1: ~ (1218 μs 8206 samples)
day2.part2: ~ (4902 μs 2040 samples)
day3.part1: ~ (273 μs 36628 samples)
day3.part2: ~ (378 μs 26463 samples)
day4.part1: ~ (15 ms 683 samples)
day4.part2: ~ (18 ms 541 samples)
day5.part1: ~ (2047 μs 4885 samples)
day5.part2: ~ (1544 μs 6475 samples)
day6.part1: ~ (2719 μs 3678 samples)
day6.part2: ~ (3375 ms 3 samples)
day7.part1: ~ (4123 μs 2426 samples)
day7.part2: ~ (7204 μs 1388 samples)
day8.part1: ~ (401 μs 24919 samples)
day8.part2: ~ (934 μs 10701 samples)
day9.part1: ~ (7753 μs 1290 samples)
day9.part2: ~ (1626 ms 7 samples)
day10.part1: ~ (12 ms 856 samples)
day10.part2: ~ (12 ms 848 samples)
day11.part1: ~ (1528 μs 6544 samples)
day11.part2: ~ (57 ms 175 samples)
day12.part1: ~ (23 ms 442 samples)
day12.part2: ~ (29 ms 350 samples)
day13.part1: ~ (6093 ms 2 samples)
day13.part2: ~ (1302 μs 7680 samples)
day14.part1: ~ (25 ms 406 samples)
day14.part2: ~ (77 ns 42725914 samples)
day15.part1: ~ (11 ms 912 samples)
day15.part2: ~ (25 ms 402 samples)
day16.part1: ~ (15 ms 669 samples)
day16.part2: ~ (47 s)
day17.part1: ~ (23 μs 434936 samples)
day17.part2: ~ (61 μs 162582 samples)
day18.part1: ~ (7798 μs 1283 samples)
day18.part2: ~ (7284 ms 2 samples)
day19.part1: ~ (105 ms 96 samples)
day19.part2: ~ (220 ms 46 samples)
day20.part1: ~ (51 ms 198 samples)
day20.part2: ~ (40 s)
day21.part1: ~ (5851 μs 1709 samples)
day21.part2: ~ (51 μs 197021 samples)
day22.part1: ~ (820 ms 13 samples)
day22.part2: ~ (3275 ms 4 samples)
day23.part1: ~ (206 ms 49 samples)
day23.part2: ~ (3161 ms 4 samples)
day24.part1: ~ (321 μs 31093 samples)
day24.part2: ~ (151 μs 66135 samples)
day25.part1: ~ (30 ms 335 samples)
day25.part2: ~ (71 ns 42950401 samples)
total: 114 s
```

## Environment

Description of my setup and how I use it.

* I use `setup.sh` for activating and configuring the python virtual environment.
* I usually have two terminals open, one for editing in NeoVim and one for running scripts/solutions. `start.sh` will create the terminal windows and setup the virtual environment in both.
* When each day's challenge is released I run `today.py` wich will download the input into `input/day{nr}.txt`. Any example inputs that I want to use I manually put under `input/day{nr}.{example nr}.txt`.
* `aoc.py` is a *runner* which will by default run functions `part1` and `part2` in `day{nr}.py` on the corresponding tests and input. `run.sh` will run this *runner* at any time when a solution is updated.
* To benchmark, `aoc.py --all --bench --hide --no-test --no-print` will hide the answers and only output the measured time for running each part on the corresponding input (also hiding any debug prints).
