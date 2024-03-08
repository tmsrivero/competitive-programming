n, m = map(int, input().split())
a = list(map(int, input().split()))

if m >= n:
    print(n)

else:
    cont = 0
    while True:
        x = a[0]
        p = iter(a)
        next(p)

        for num in p:
            if x > num:
                cont += 1
            else:
                break
        
        if cont >= m:
            print(x)
            break
        else:
            cont = 1
            a.popleft()
            a.append(x)