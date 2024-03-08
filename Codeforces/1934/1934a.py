# (ai -aj)+(aj-ak)+(ak-al)+(al-ai)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    i = a[0]
    j = a[n-1]
    k = a[1]
    l = a[n-2]

    c = abs(i-j)+abs(j-k)+abs(k-l)+abs(l-i)

    print(c)
