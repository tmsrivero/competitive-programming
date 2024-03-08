t = int(input())

for i in range(t):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    
    d = 0
    d = abs(a[0]-b[0]) + abs(a[1]-b[1])

    if(a[0]==b[0]) and (c[0]==a[0]):
        if (a[1]>c[1] and b[1]<c[1]) or (a[1]<c[1] and b[1]>c[1]):
            d += 2
    elif(a[1]==b[1]) and (c[1]==a[1]):
        if (a[0]>c[0] and b[0]<c[0]) or (a[0]<c[0] and b[0]>c[0]):
            d += 2
    
    print(d)