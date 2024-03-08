p = int(input())
n = int(input())

n2 = [0]*n

for i in range (n):
    n2[i] = int(input())

q = True

for i in range (n-1):
    if (n2[i]-n2[i+1]) > p:
        q = False
    elif (n2[i+1]-n2[i]) > p:
        q = False

if(q==True):
    print("YOU WIN")
else:
    print("GAME OVER")
