n = int(input())
a = ""
b = ""
if n >= 4:
    if n % 2 == 0:
        for i in range(1, n, 2):
            a += f"{i} "
            b += f"{i+1} "
    else:
        for i in range(1, n, 2):
            a += f"{i} "
            b += f"{i+1} "
        a += f"{n} "

    print(b+a)

elif n == 1:
    print(1)
else:
    print("NO SOLUTION")
