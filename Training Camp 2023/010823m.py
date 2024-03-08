a = [0]*4
for i in range(4):
    a[i] = int(input())

if (a[2]>= 1 and a[0] == a[3] and a[0] >= 1 and a[3] >= 1):
    print(1)
elif (a[3] == a[0] and a[2] == 0):
    print(1)
else:
    print(0)