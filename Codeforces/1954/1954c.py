def minor(M, m, i):
    a1 = a2 = str()
    for k in range(0, i):
        a1 += M[k]
        a2 += m[k]
    for j in range(i, len(m)):
        a2 += max(M[j], m[j])
        a1 += min(M[j], m[j])
    print(a1)
    print(a2)


t = int(input())
for _ in range(t):
    x = str(input())
    y = str(input())
    if x == y:
        print(x)
        print(y)
    else:
        i = 0
        ban = True
        while ban == True:
            if x[i] != y[i]:
                ban = False
                if x[i] > y[i]:
                    minor(x, y, i)
                else:
                    minor(y, x, i)
            else:
                i += 1
