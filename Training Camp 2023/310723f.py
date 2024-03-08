import math

def area_of_shitalia(n, R, r):
    outer_area = n * (R ** 2) * math.sin(2 * math.pi / n) / 2

    inner_area = n * (r ** 2) * math.sin(2 * math.pi / n) / 2

    shitalia_area = outer_area - inner_area

    return shitalia_area

n, R, r = map(int, input().split())

print("{:.6f}".format(area_of_shitalia(n, R, r)))
