t = int(input())
for i in range(t):
    j = int(input())
    d = {"00": 10**9, "01": 10**9, "10": 10**9, "11": 10**9}
    for j in range(j):
        x, y = input().split()
        x = int(x)
        d[y] = min(d[y], x)
    if min(d["11"], d["10"] + d["01"]) > 10**8:
        print("-1")
    else:
        print(min(d["11"], d["10"] + d["01"]))