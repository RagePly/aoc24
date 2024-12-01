#!/bin/env python3
from html.parser import HTMLParser
from re import sub, finditer, MULTILINE
from pathlib import Path
from requests import get
from itertools import accumulate

import matplotlib.pyplot as plt
import os, time

def load_dotenv():
    dotenv_p = Path(".env")

    if not dotenv_p.is_file():
        print("NOTE: .env not found")
        return

    with open(dotenv_p, "r") as fp:
        for m in finditer(r"^([a-zA-Z][a-zA-Z_0-9]*)=(.*)$", fp.read(), flags=MULTILINE):
            if not m[1] in os.environ:
                os.environ[m[1]] = m[2]

class ScoreParser(HTMLParser):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.is_personal_leaderboard = False
        self.scores_text = []

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.is_personal_leaderboard = True

    def handle_endtag(self, tag):
        if tag == "pre":
            self.is_personal_leaderboard = False

    def handle_data(self, data):
        if self.is_personal_leaderboard:
            self.scores_text.append(data)

    def get_scores(self):
        return "".join(self.scores_text)

OK = "\x1b[32mok\x1b[m"
ERROR = "\x1b[31merror\x1b[m"

def begin_log(*args): print(*args, end="...")
def end_log(*args): print(*args)

def main():
    begin_log("check rate limit")
    # check that requests are limited to once every 15-minutes
    cache_folder = Path(os.getenv("HOME")) / ".cache"
    timestamp = cache_folder / "aoc_scores_ts"
    cache = cache_folder / "aoc_scores_data"
    use_cached = False

    if timestamp.exists():
        try:
            with open(timestamp, "r") as fp:
                ts = float(fp.read())
        except ValueError:
            raise AocError("timestamp file was incorrectly formatted")

        if time.time() - ts < 15 * 60:
            end_log(ERROR)

            if not cache.exists():
                print("error: requests are limited to once every 15 minutes")
                exit(1)
            else:
                print(f"using cached data in {cache}")
                use_cached = True
        else:
            end_log(OK)
    else:
        cache_folder.mkdir(parents=True, exist_ok=True) 

    if use_cached:
        with open(cache) as fp:
            score_text = fp.read()
    else:
        print("fetching new data.")
        begin_log("loading .env")
        load_dotenv()
        end_log(OK)

        if not "AOC_SESSION" in os.environ:
            print("error: session token not found, "
                  "use environment variable AOC_SESSION=<token>")
            exit(1)
        begin_log("fetching data")
        cookies = {
            "session": os.environ["AOC_SESSION"],
        }
        resp = get("https://adventofcode.com/2024/leaderboard/self", cookies=cookies)

        if not resp.status_code == 200:
            end_log(ERROR)
            print(f"error: got status code {resp.status_code} from adventofcode.com")
            exit(1)
        end_log(OK)

        parser = ScoreParser()
        parser.feed(resp.text)
        score_text = parser.get_scores()
    
        with open(timestamp, "w") as fp:
            fp.write(str(time.time()))

        print(f"cache:ing response in {cache}")
        with open(cache, "w") as fp:
            fp.write(score_text)
    
    begin_log("rendering scores")
    part_header, column_headers, *scores = score_text.splitlines()

    ranking = []
    times = []
    for score in scores:
        days, t1, r1, _, t2, r2, _ = score.split()
        times.append(time.strptime(t1, "%H:%M:%S"))
        times.append(time.strptime(t2, "%H:%M:%S"))
        ranking.append(int(r1))
        ranking.append(int(r2))

    days = list(range(1, int(days) + 1))
    positions = [x for d in days for x in [d - 0.2, d + 0.2]]
    plt.bar(
        positions,
        ranking,
        0.38,
        0,
        color = [c for _ in ranking for c in ["#9999cc", "#ffff66"]]
    )

    for r, p, t in zip(ranking, positions, times):
        if t.tm_hour > 0:
            ts = f"{t.tm_hour}h {t.tm_min}m {t.tm_sec}s"
        else:
            ts = f"{t.tm_min}m {t.tm_sec}s"
        plt.text(p, r, f"\n{r}\n{ts}", ha="center", va="top")
    ticks = list(range(1000, max(ranking) + 1000, 1000))
    plt.yticks(ticks)
    plt.xticks(days, [f"Day {d}" for d in days])
    plt.plot([1 - 0.4, max(days) + 0.4], [1000, 1000], label="Goal", color = "red")
    avg_score = [avg[0] for avg in accumulate(
            ranking[1::2],
            lambda a, x: (((a[1] * a[0]) + x) / (a[1] + 1), a[1] + 1),
            initial=(0, 0)
            )][1:]
    plt.text(days[-1] + 0.25, avg_score[-1], f"{int(avg_score[-1])}", va="center", ha="left")
    plt.plot(
        [d + 0.2 for d in days],
        avg_score,
        label = "Average ranking")

    # Taken from https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
    # #############################################################################################
    # Shrink current axis by 20%
    ax = plt.gca()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    # #############################################################################################

    plt.title("Scores")

    Path("./res").mkdir(exist_ok=True)
    plt.savefig("res/scores.png")

    end_log(OK)

    begin_log("updating README.md")
    with open("README.md", "r+") as fp:
        readme = fp.read()
        new_readme = sub(r"```\{scores\}[^`]*```", 
            f"```{{scores}}\n{score_text}\n```",
            readme)
        fp.seek(0)
        fp.write(new_readme)
    end_log(OK)

if __name__ == "__main__":
    main()
