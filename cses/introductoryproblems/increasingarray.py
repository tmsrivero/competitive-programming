n = int(input())
a = list(map(int, input().split()))
cont = 0
for i in range(n-1):
    if a[i] > a[i+1]:
        cont += (a[i]-a[i+1])
        a[i+1] += (a[i]-a[i+1])
print(cont)
