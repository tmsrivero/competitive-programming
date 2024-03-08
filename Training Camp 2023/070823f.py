n = int(input())
a = list(map(int,input().split()))

s =set()

for i in range(n):
    if a[i]<= n:
        s.add(a[i])

sum = n - len(s)


print(sum)