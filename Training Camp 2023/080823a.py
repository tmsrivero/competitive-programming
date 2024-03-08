n = int(input())
a = list(map(int,input().split()))
a.sort()
cont = 1
max = 1
for i in range(len(a)-1):
    if (a[i]==a[i+1]):
        cont += 1
        if cont>max:
            max = cont
    else:
        cont = 1

print(max)
    