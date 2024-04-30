t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0] == n
    for i in range(n):
        ans = ans and (i + 1) <= a[a[i] - 1]
    if ans:
        print("YES")
    else:
        print("NO")
