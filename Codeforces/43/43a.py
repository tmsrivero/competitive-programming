t = int(input())
d = {}
ban = False
for _ in range(t):
    n = input()
    if n not in d.keys():
        d[n] = 1
    else:
        d[n] += 1

m = max(d, key=d.get)
print(m)
