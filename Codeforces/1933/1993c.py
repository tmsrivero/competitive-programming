t = int(input())
for _ in range(t):
    a, b, l = map(int, input().split())
    factors = set()
    for x in range(101):
        for y in range(101):
            if a ** x * b ** y > l:
                break
            if l % (a ** x * b ** y) == 0:
                factors.add(l // (a ** x * b ** y))
    result = len(factors)
    print(result)
