t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 != 0:
        print("Mike")
    else:
        b = sorted(a)
        min = b[0]
        m = a.index(min)
        if m % 2 == 0:
            print("Joe")
        else:
            print("Mike")
