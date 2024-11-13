'''
File that will:
Load graphs for all generated inputs in `./data` and run the solution on them one at a time.
'''

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), './sol'))

from none import none # type: ignore
from alternate import alternate # type: ignore
from few import few # type: ignore
from some import some # type: ignore

# Defining main function
def main():
    files = os.listdir('./data')
    problems = [none(), alternate(), few(), some()]

    for file in files:
        if file.endswith('.txt'):
            print('Loading', file)
            for problem in problems:
                problem.run("./data/" + file)

if __name__=="__main__":
    main()
