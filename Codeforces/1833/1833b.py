t = int(input())

for i in range(t):

    n,k = map(int,input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [0]*n
    
    for j in range(n):
        ban = False
        for r in range(n):
            if (abs(a[j] - b[r]) <= k and ban == False):
                c[j] = b[r]
                b[r] = 10**9
                ban = True

    print(*c)
        

