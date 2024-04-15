a = input()
b = a.capitalize()
c = a.upper()

if a == c:
    print(a.lower())
else:
    ban = False
    for i in range(len(a)):
        if a[i] == b[i]:
            ban = True
    if ban == True:
        print(a)
    else:
        print(b)
