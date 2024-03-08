k,n,w = map(int,input().split())
sum = 0
for i in range(w):
    sum = sum + (k*(i+1))

if (sum<=n):
    print(0)
else:
    print(sum-n)