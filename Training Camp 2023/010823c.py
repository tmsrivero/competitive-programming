def invertir_cadena(cadena):
    return cadena[::-1]

k, p = map(int,input().split())
cont = 0
for i in range(k):
    pal = str((i+1)) + invertir_cadena(str(i+1))
    cont += int(pal)

r = cont % p
print(r)