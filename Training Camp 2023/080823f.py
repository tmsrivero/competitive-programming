n = input()
cont = 0
ca = 0
cb = 0
l = len(n)
for i in range(l):
    if n[i] == "Q":
        cont += ca
        cb += 1
    elif n[i] == "A":
        ca += cb

print(cont)