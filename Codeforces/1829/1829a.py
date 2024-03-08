t = int(input())
c = "codeforces"
 
for i in range(t):
    cont = 0
    a= input()
    for j in range(10):
        if(c[j]!= a[j]):
            cont = cont + 1
    print(cont)