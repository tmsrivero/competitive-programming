#si todos son - 25 = nadie rechazó
#si hay uno + 25 = alguien rechazó

c = 0
n = int(input())

alu = list(map(int,input().split()))

alu.sort()

if (alu[n-1] <= 25):
    print(c)
else:
    if (alu[0] != 1):
        c = c + (alu[0]-1)
    for i in range(n-1):
        if (alu[i+1] == alu[i]+1):
            c = c
        else:
            c = c + (alu[i+1] - alu[i]) - 1
    
    print(c-(25-n))
