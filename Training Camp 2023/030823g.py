t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    s = set()
    for j in range(len(l)):
        if (j%2 == 0):
            s.add(j)
    r = 0  
    while len(s)!=0:
        k = s.pop()
        r += 1
        if k//2 % 2 == 0:
            s.add(k//2)
    
    print(r)
