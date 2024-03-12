def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-2):
        if a[i] < 0:
            print("NO")
            return
        op = a[i]
        a[i] -= op
        a[i+1] -= 2*op
        a[i+2] -= op
    if a[-1] != 0 or a[-2] != 0:
        print("NO")
    else:
        print("YES")


for _ in range(int(input())):
    solve()
