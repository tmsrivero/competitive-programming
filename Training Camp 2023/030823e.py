n,m = map(int,input().split())
r = 0

if (m%n != 0):
    r = -1
    print(r)
else:
    if (m==n):
        r = 0
        print(r)
    else:
        s = m/n
        while (s%2==0):
            s = s/2
            r = r+1
        while (s%3==0):
            s = s/3
            r = r+1

        if (s != 1):
            r= -1
            print(r)
        else:
            print(r)