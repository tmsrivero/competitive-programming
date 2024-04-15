t = int(input())
for _ in range(t):
    s = input()
    c1 = s.count("1")
    c0 = s.count("0")
    c = 0
    for i in range(len(s)):
        if (s[i] == "1"):
            if c0 == 0:
                c = len(s) - i
                break
            else:
                c0 -= 1
        elif (s[i] == "0"):
            if (c1 == 0):
                c = len(s) - i
                break
            else:
                c1 -= 1
    print(c)
