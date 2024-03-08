def is_beautiful(n, a):
    minpar = False
    posible = True

    minimo = min(a)
    if minimo % 2 == 0:
        minpar = True

    if (minpar == True):    
        for j in range(n):
            if a[j] % 2 == 0:
                posible = True
            elif ((a[j] - minimo) % 2 == 0):
                posible = True
            else:
                posible = False
                break
    else: 
        for j in range(n):
            if a[j] % 2 != 0:
                posible = True
            elif ((a[j] - minimo) % 2 != 0):
                posible = True
            else:
                posible = False
                break

    if (posible == False):
        return "NO"
    else:
        return "YES"

t = int(input()) 

for i in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  

    result = is_beautiful(n, a)
    print(result)