n = int(input())
a = list(map(int, input().split()))
prefixSum = [0 for i in range(n)]
prefixSum[0] = a[0]
for i in range(1, n):
    prefixSum[i] = prefixSum[i - 1] + a[i]
q = int(input())
for _ in range(q):
    i, j = map(int, input().split())
    if i != 0:
        print(prefixSum[j]-prefixSum[i-1])
    else:
        print(prefixSum[j])
