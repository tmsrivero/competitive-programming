def suma(int(d),int(m)):
    r = sum((((10 ^ (d-1)) - 1) * 10) + (45 * (10 ^ (d-1))))
    mul = r*(int(m))
    return mul


t = int(input())
for _ in range(t):
    n = int(input())
    suma(len(str(n)), str(n)[0])
