import math


def binary(x):
    l = 1
    r = 10e9
    while l <= r:
        mid = l + (r-l) // 2
        if mid * mid == x:
            return True
        elif mid * mid > x:
            r = mid - 1
        else:
            l = mid + 1
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    a = list(map(int, input().split()))
    for i in range(len(a)):
        s += a[i]
    if binary(s):
        print("YES")
    else:
        print("NO")
