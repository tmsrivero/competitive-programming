a, b, x = map(int, input().split())
r = ""
g = (a > b)
while x >= 0:
    if (g==True):
        if a > 0:
            r += "0"
            a -= 1
    else:
        if b > 0:
            r += "1"
            b -= 1
    g = not g
    x -= 1
while a > 0:
    for i in range(len(r)):
        if r[i] == "0":
            r = r[:i] + "0" + r[i:]
            break
    a -= 1
while b > 0:
    for i in range(len(r)):
        if r[i] == "1":
            r = r[:i] + "1" + r[i:]
            break
    b -= 1
print(r)