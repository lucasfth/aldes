n_points = int(input())

points = []

for _ in range(n_points):
    x, y = map(float, input().split())
    points.append([x, y])

points.sort(key=lambda x: x[0])  # sort by x


def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


def distance(points):
    mid = points[len(points)//2][0]

    if (len(points) == 2):
        return (dist(points[0], points[1]), points)
    elif (len(points) == 3):
        dist_min, point_min = dist(points[0], points[1]), (points[0], points[1])
        if dist(points[0], points[2]) < dist_min:
            dist_min, point_min = dist(points[0], points[2]), (points[0], points[2])
        elif dist(points[1], points[2]) < dist_min:
            dist_min, point_min = dist(points[1], points[2]), (points[1], points[2])
        return (dist_min, point_min)

    delta_l = distance(points[:len(points)//2])
    delta_r = distance(points[len(points)//2:])
    delta = delta_l if delta_l[0] < delta_r[0] else delta_r

    short = [point for point in points if abs(point[0] - mid) < delta[0]]

    short.sort(key=lambda y: y[1])

    for i in range(len(short)):
        for j in range(i+1, min(i+2, len(short))):
            if dist(short[i], short[j]) < delta[0]:
                delta = (dist(short[i], short[j]), (short[i], short[j]))

    return delta


res = distance(points)

print(res[1][0][0], res[1][0][1])
print(res[1][1][0], res[1][1][1])
