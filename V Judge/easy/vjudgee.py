s = input()
word = "hello"
j = 0
for i in range(len(s)):
    if s[i] == word[j]:
        j += 1
    if j == 5:
        break

if j == 5:
    print("YES")
else:
    print("NO")
