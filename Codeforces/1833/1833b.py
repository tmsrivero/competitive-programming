t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = sorted(a)
    d = sorted(b)
    e = [0]*n
    for i in range(len(a)):
        p = a.index(c[i])
        a[p] = 10 ^ 10
        e[p] = d[i]

    for item in e:
        print(item, end=" ")
