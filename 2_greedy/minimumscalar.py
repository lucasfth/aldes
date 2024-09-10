scalarAmount = int(input())
for _ in range(scalarAmount):
    int(input())
    v1 = list(map(int, input().split(' ')))
    v1.sort()
    v2 = list(map(int, input().split(' ')))
    v2.sort(reverse=True)
    sum = 0
    for v1, v2 in zip(v1, v2):
        sum += v1 * v2
    print(f'Case #{_+1}: {sum}')
