n, cap, dif = map(int, input().split())
socks = list(map(int, input().split()))
socks.sort()

washes = 1
amount = 0
cur = socks[0]

for sock in socks:
    if abs(cur - sock) <= dif and cap > amount:
        amount += 1
    else:
        cur = sock
        washes += 1
        amount = 1

print(washes)
