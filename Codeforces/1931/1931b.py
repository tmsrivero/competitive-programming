t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list()
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i-1]+a[i]

    if (b[n]/n == int):
        print("yes")
    else:
        print("No")
