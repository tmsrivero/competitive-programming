
i = int(input())
 
for i in range(i):
    n = int(input())
    f = list(map(int, input().split()))
 
    maxima = max(f)
    segundo = 0
    m = [0]*n
    rep = False
    for j in range(n):
        if ((f[j]!=maxima or rep==True) and f[j]>segundo):
            segundo = f[j]
        if f[j]==maxima:
            rep = True
 
    for k in range(n):   
        if (f[k]!= maxima):
           m[k] = f[k] - maxima
        else:
           m[k] = maxima - segundo
    print(*m)
 