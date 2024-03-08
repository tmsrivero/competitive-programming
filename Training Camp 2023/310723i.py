a = ["Power","Time","Space","Soul","Reality","Mind"]
b = [0,0,0,0,0,0]

n = int(input())
for i in range(n):
    p = input()
    if (p == "purple"):
        b[0] = 1
    elif (p == "green"):
        b[1] = 1 
    elif (p == "blue"):
        b[2] = 1 
    elif (p == "orange"):
        b[3] = 1 
    elif (p == "red"):
        b[4] = 1 
    elif (p == "yellow"):
        b[5] = 1         

print(6-n)
for j in range(6):
    if (b[j]==0):
        print(a[j])