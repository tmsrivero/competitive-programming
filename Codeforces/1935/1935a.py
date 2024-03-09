t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s2 = s[::-1] + s
    ban = True
    i = 0
    while ban and i < len(s):
        if s[i] < s2[i]:
            a = s
            ban = False
        elif s2[i] < s[i]:
            a = s2
            ban = False
        i += 1

    if ban == True:
        print(s)
    else:
        print(a)
