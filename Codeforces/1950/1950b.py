t = int(input())
for _ in range(t):
    n = int(input())
    ban = True
    c = 0
    for i in range(2*n):
        a = ""
        rr = ban
        for i in range(n):
            if ban == True:
                a += "##"
                ban = False
            else:
                a += ".."
                ban = True
        print(a)
        ban = rr
        c += 1
        if c == 2:
            if ban == True:
                ban = False
                c = 0
            else:
                ban = True
                c = 0
