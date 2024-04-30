t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = list(map(int, input().split()))
    s += s
    for i in range(len(s)):
        