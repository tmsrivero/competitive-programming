i = int(input())
 
for i in range(i):
    a, b, c = map(int,input().split())
 
    max_num = max(a,b,c)
    min_num = min(a,b,c)
 
    if (a!=max_num) and (a!=min_num):
        print(a)
    elif (b!=max_num) and (b!=min_num):
        print(b)
    else:
        print(c)