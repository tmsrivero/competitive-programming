n = int(input())
while n != 0:
    p = [0]*n
    c = 0
    for i in range(n):
        p[i]= int(input())

    for i in range(0,n):
        if p[i] == 0 and p[i+1] == 0:
            p[i+1] == 1
            if p[i+2] == 0:
                p[i+2] = 1
            c = c+1
        
    print (c)
    n = int(input())