t = int(input())
r = 0
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    mid = (n-1)//2
    max = max(a)
    imax = a.index(max)
    min = min(a)
    imin = a.index(min)
    
    dmin = mid - imin
    dmax = mid - imax
    if (dmin < 0):
        dmin = -dmin
    if (dmax < 0):
        dmax = - dmax
    print(dmax,dmin)

