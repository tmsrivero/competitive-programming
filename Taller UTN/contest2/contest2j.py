t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    s = (a + b + c) // 9
    if s <= min(a, min(b, c)) and (a + b + c) % 9 == 0:
        print("YES")
    else:
        print("NO")
