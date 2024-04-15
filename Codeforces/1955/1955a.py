t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    c = a*2
    if n % 2 == 0:
        if c < b:
            print(int(c*(n/2)))
        else:
            print(int(b*(n/2)))
    else:
        if c < b:
            print(int(c*(n//2)) + a)
        else:
            print(int(b*(n//2)) + a)
