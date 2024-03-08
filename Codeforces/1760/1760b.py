i = int(input())
 
a = "abcdefghijklmnopqrstuvwxyz"
 
for i in range(i):
    n = int(input())
    c = input()
    
    maximo = max(c)
 
    igual = True
    j = 0
    while (igual == True) and (j != 26):
        if (a[j] == maximo):
            igual = False
        j = j+1
    print(j) 