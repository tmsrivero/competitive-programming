d = 0
x = list(map(int,input().split()))
x.sort()

d = (x[1]-x[0]) + (x[2]-x[1])

print(d)
