import math
n = int(input())
m = int(input())
q = True
while q != False:
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        n = n - 1
    elif n > 7:
        if n%7 == 0:
            n = n - 1
    else:
        0
    if m%2 == 0 or m%3 == 0 or m%5 == 0:
        m = m - 1
    else:
        0
    if n%2 != 0 and n%3 != 0 and n%5 != 0 and m%2 != 0 and m%3 != 0 and m%5 != 0:
        q = False

mult = n * m
print (mult)