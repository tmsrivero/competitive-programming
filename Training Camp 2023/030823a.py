def bs(L, target):
    p = 0
    f = len(L) - 1
    r = 0

    while p <= f:
        medio = (p + f)// 2
        medioarray = L[medio]
        if (medioarray.startswith(target)):
            r = 1
            break
        elif (medioarray > target):
            f = medio - 1
        else:
            p = medio + 1
        
    return r

t = int(input())
a = []
for i in range(t):
    mn= input().split()
    m = mn[0]
    if (len(mn)> 1):
        n = mn[1]
    
    if (m=="1"):
        a.append(n)
        a.sort()
    elif (m=="2"):
        print(bs(a,n))
             
    elif (m=="3"):
        for j in range(len(a)):
            a[j] = a[j] [::-1]