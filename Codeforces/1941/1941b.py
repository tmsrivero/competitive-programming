t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[1] - (2*a[0]) == 1 and a[n-2] - (2*a[n-1]) == 1:
        print("YES")
    else:
        print("NO")
