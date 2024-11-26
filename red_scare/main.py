"""
File that will:
Load graphs for all generated inputs in `./data` and run the solution on them one at a time.
"""

import time
from tabulate import tabulate
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "./sol"))

from none import none  # type: ignore
from alternate import alternate  # type: ignore
from few import few  # type: ignore
from some import some  # type: ignore
from many import many  # type: ignore

sys.setrecursionlimit(100000)


# Defining main function
def main():
    files = os.listdir('./data')
    problems = [none(), alternate(), few(), some(), many()]
    running_time = [["File"] + [p.__class__.__name__ for p in problems]]

    for file in files:
        if file.endswith('.txt'):
            print('Loading', file)
            row = [file]
            for problem in problems:
                s_t = time.time()
                res = problem.run("./data/" + file)
                e_t = time.time()
                print(f"\t{problem.__class__.__name__}: {res}")
                delta = e_t - s_t
                row.append(f"s: {res} - t: {delta:.6f}s")
            running_time.append(row)

    print(tabulate(running_time, headers="firstrow", tablefmt="grid"))

    with open("./results.txt", "w") as f:
        f.write(tabulate(running_time, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
