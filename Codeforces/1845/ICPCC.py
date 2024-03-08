a = [[0]*2023 for i in range(2023)]
a[0][0] = 1

def solucion():
    for j in range(1,2023):
        for i in range(i+1):
            a[j][i] = a[j][i-1]








#c = int(input())
#for z in range(c):
#    solucion()