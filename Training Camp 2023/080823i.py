t = int(input())

for i in range(t):
    s= input()
    ban = 1
    bana = 0
    banb = 0
    ca = 0
    cb = 0
    if s[0] == "B":
        ban = 0
    elif s[len(s)-1] == "A":
        ban = 0
    else:
        for j in range(1,(len(s)-1)):
            if s[j]=="B":
                if banb == 0:
                    bana = 0
                    banb = 1
                    cb = 0
                cb =+ 1
                if cb>ca:
                    ban = 0
                    break
            else:
                if bana == 0:
                    banb = 0
                    bana = 1
                    ca = 0
                ca += 1
    if ban==1:
        print("YES")
    else:
        print("NO")