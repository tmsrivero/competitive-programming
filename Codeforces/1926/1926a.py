t = int(input())
for _ in range(t):
    s = input()
    acont = 0
    bcont = 0
    for i in range(5):
        if (s[i] == "A"):
            acont += 1
        else:
            bcont += 1

    if acont > bcont:
        print("A")
    else:
        print("B")
