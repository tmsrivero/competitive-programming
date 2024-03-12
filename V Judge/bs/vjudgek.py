def binarySearch(arr, l, r, x):

    while l <= r:

        m = l + (r - l) // 2

        if arr[m] == x:
            try:
                while arr[m] == arr[m-1]:
                    m -= 1
                return m
            except:
                return m

        elif arr[m] < x:
            l = m + 1

        else:
            r = m - 1

    return -1


n, q = map(int, input().split())
a = list(map(int, input().split()))
n = n-1
p = 0
f = n
m = n // 2
for i in range(q):
    query = int(input())
    print(binarySearch(a, 0, n, query))
