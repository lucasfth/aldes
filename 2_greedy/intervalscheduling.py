intervals = int(input())

lst = []

for _ in range(intervals):
    i, j = map(int, input().split(' '))
    lst.append((i, j))

lst.sort(key=lambda x: x[1])

count = 0
end_time = 0

for _ in range(intervals):
    if lst[0][0] >= end_time:
        count += 1
        end_time = lst[0][1]
    lst.pop(0)

print(count)
