mayor = 0
suma = 0
n = int(input())
m = int(input())
array = []

for i in range(n):
    aux = []
    for j in range(m):
        num = int(input())
        aux.append(num)
    array.append(aux)
for i in range(n):
    suma = 0
    for j in range(m):
        suma = suma + array[i][j]
        if suma > mayor:
            mayor = suma

for i in range(m):
    suma = 0
    for j in range(n):
        suma = suma + array[j][i]
        if suma > mayor:
            mayor = suma

print(mayor)