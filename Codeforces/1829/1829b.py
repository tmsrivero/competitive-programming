t = int(input())
 
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_len = 0
    curr_len = 0
    for j in range(n):
        if a[j] == 0:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 0
    max_len = max(max_len, curr_len)
    print(max_len)