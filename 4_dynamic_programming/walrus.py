n = int(input())

closest_value = float('inf')

weights = [int(input()) for _ in range(n)]

max = 2000
solutions = [False] * (max + 1)
solutions[0] = True

for w in weights:
    for i in range(max, w-1, -1):
        if solutions[i-w]:
            solutions[i] = True

# print([(i, s) for i, s in enumerate(solutions) if s])

bw = 0


def closest_weight(a, b):
    a_abs = abs(a - 1000)
    b_abs = abs(b - 1000)

    if a_abs < b_abs:
        return a
    elif a_abs > b_abs:
        return b
    elif a_abs == b_abs:
        return a if a > b else b


for i, b in enumerate(solutions):
    if b:
        bw = closest_weight(bw, i)

print(bw)
