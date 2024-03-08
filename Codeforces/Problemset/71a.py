n = int(input())

for i in range(n):
    w = input()
    if (len(w)>10):
        l = str(len(w)-2)
        print( w[0] + l + w[len(w)-1])
    else:
        print(w)