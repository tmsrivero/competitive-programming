n = input()
max = 1
cont = 1
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        cont += 1
        if cont > max:
            max = cont
    else:
        cont = 1

print(max)
