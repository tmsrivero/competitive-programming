mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def evaluar(n, resto):
    ban = True
    num = 1
    while (ban == True):
        if (resto < (n-num)):
            num = num+1
        else:
            ban = False
    return num


t = int(input())
for i in range(t):
    n = int(input())
    first = evaluar(n, 52)
    second = evaluar(n-first, 26)
    third = n-first-second
    print(mylist[first-1]+mylist[second-1]+mylist[third-1])
