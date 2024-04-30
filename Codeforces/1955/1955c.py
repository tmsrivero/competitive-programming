t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n//2):
        for j in range(n-1, n//2 - 1, -1):
            ban = False
            if (k - a[i] >= 0):
                k -= a[i]
                ans += 1
                ban = True

            if k - a[j] >= 0:
                k -= a[j]
                ans += 1
                ban = True

            if ban == False:
                break

    print(ans)
