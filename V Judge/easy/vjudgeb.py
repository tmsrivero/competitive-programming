cont = 0
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    b = a[0] + a[1] + a[2]
    if b >= 2:
        cont += 1

print(cont)
