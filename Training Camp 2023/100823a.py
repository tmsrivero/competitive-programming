t = int(input())

def fmex(s):
    mex = 0
    while mex in s:
        mex += 1
    return mex


for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a)
    maxval = max(a)
    
    if maxval == n - 1:
        print(n + k)
        continue
    
    mex = fmex(s)

    u = (maxval + mex + 1) // 2
    add = (k > 0) * (1 - int(u in s))
    print(len(s) + add)