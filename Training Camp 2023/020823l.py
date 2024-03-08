t = int(input())

for i  in range(t):
    n = int(input())
    a = input()
    r = 0
    o = 0
    c = 0

    for i in range(n):
        if a[i] == "(":
            o += 1
        elif a[i] == ")":
            c += 1

        if ((c - o) >= r):
            r = c-o
    
    print(r)
    
