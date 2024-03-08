from calendar import c


R = int(input())
X = (R*2) + 1
N = [[0] * X] * (R+1)
A = X // 2
A = A+1
for i in range (R):
    while A-c != 0:
        B = A-c
        d = A + c
    if i == 0:
        N[i][B] = 1
    if i == 1:
        N[i][A] = 1
        N[i][A-1] = 1
        N[i][A+1] = 1
    elif A == 0:
        N[i][A] = N[i+1][A] + N[i+1][A+1] 
    elif A+1 == X:
        N[i][A] = N[i+1][A] + N[i+1][A-1]
    else:
        N[i][A-c] = N[i+1][A] + N[i+1][A+1] + N[i+1][A-1]
        N[i][A+c] = N[i+1][A] + N[i+1][A+1] + N[i+1][A-1]
        N[i][A] = N[i+1][A] + N[i+1][A+1] + N[i+1][A-1]
        
print (N)
Z = 0
for i in range (X):
    Z = Z + N[R][i]
print (Z)