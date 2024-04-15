n = int(input())
a = f"{n}"
while (n != 1):
    if n % 2 == 0:
        n = n//2
        a += f" {n}"
    else:
        n = n*3+1
        a += f" {n}"

print(a)
