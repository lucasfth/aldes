'''
File that will:
Load graphs for all generated inputs in `./data` and run the solution on them one at a time.
'''

import sys
import os
import threading
sys.path.append(os.path.join(os.path.dirname(__file__), './sol'))

from none import none # type: ignore
from alternate import alternate # type: ignore

# Defining a function to run a problem on a file
def run_problem(problem, file):
    problem.run(file)

# Defining main function
def main():
    files = os.listdir('./data')
    problems = [none(), alternate()]
    threads = []

    for file in files:
        if file.endswith('.txt'):
            print('Loading', file)
            for problem in problems:
                thread = threading.Thread(target=run_problem, args=(problem, "./data/" + file))
                threads.append(thread)
                thread.start()
            
            # Wait for all the problems to finish with the current file
            for thread in threads:
                thread.join()


if __name__=="__main__":
    main()