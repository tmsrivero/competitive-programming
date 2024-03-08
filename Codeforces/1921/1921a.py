a = int(input())
for i in range(a):
    arr = []
    for i in range(4):
        a, b = map(int, input().split())
        if a not in arr:
            arr.append(a)

    if len(arr) > 1:
        lado = abs(arr[0]-arr[1])
        rta = lado*lado
        print(rta)
    else:
        print("0")
