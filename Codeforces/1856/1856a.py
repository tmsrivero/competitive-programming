def buscamax(a):
    max = 0
    imax = 0
    maxcount = 0
    for i in range(len(a)):
        if(a[i]>=max):
            max = a[i]
            imax = i
            maxcount += 1
    return imax, max, maxcount

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    r = 0

    ban = False
  
    while (ban!=True):
        buscamax(a)
        imax, max, maxcount= buscamax(a)
        if(imax != (len(a)-1) and (maxcount!= len(a))):
            r = max
            ban = True
        elif(len(a)==1):
            ban = True
        elif(maxcount==len(a)):
            ban = True
        else:
            a.pop(imax)
        
    print(r)

            
