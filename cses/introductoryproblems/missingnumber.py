n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
ban = False
for i in range(len(a)-1):
    if a[i]+1 != a[i+1]:
        print(a[i]+1)
        ban = True
        break
if ban != True and a[0] == 1:
    print(a[-1]+1)
elif ban != True and a[0] != 1:
    print(1)
