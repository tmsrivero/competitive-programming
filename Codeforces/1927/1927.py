t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sa = 0
    sb = 0
    sc = 0
    for i in range(1, k+1):
        if (i in a) and (i not in b):
            sa += 1
        if (i not in a) and (i not in b):
            sa = k
            break

        if sa > (k/2):
            print("NO")
        else:
            print("YES")
