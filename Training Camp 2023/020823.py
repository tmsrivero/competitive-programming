n = int(input())
s = list(input())
cont = 0
for i in range (0,n-1,2):
    if (s[i] == s[i+1]):
        s[i] = "a"
        s[i+1] = "b"
        cont += 1

print(cont)
print("".join(s))
