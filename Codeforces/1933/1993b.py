t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    ban = False
    for i in range(n):
        while (ban == False):
            if (a[i] % 3 == 1):
                ban = True
            break
        c += a[i]
    if (c % 3 == 0):
        print(0)
    elif (((c-1) % 3 == 0 and ban == True) or (c+1) % 3 == 0):
        print(1)
    else:
        print(2)
