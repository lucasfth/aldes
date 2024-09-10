import sys
from math import sqrt

# NOT WORKING


def intersection(radius, width):
    return sqrt(radius**2-(width/2)**2)


def calc():
    sprinklers, grass_length, grass_width = map(int, (input().split(' ')))
    # print("Sprinkler ${sprinklers}, Grass Length ${grass_length}, Grass Width ${grass_width}")

    lst = []

    for _ in range(sprinklers):
        p, r = map(int, input().split(' '))
        # print("")
        # print(f"p, r: ${p}, ${r}")
        intersect = intersection(r, grass_width)
        # print(f"\tintersect: ${intersect}")
        i, j = p - intersect, p + intersect
        # print(f"\ti, j: ${i}, ${j}")
        lst.append((i, j))

    lst.sort(key=lambda x: x[0])
    # print("Sorted List\n")
    # print(lst)

    count = 0
    end_time = 0

    # print("List")
    while end_time <= grass_length:
        if (len(lst) == 0):
            print(-1)
            sys.exit()

        index, max = -1, -1
        for idx, (i, j) in enumerate(lst):
            if i <= end_time and j > max:
                max = j
                index = idx
        # print()
        # print(f"Element: ${idx} - index ${index}, max ${max}")
        end_time = max
        count += 1
        lst.pop(index)

    # print(lst)

    print(count)


while sys.stdin.readline:
    calc()
