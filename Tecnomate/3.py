H = int(input())
W = int(input())
A = [[""] * W] * H
for i in range(H):
    for j in range(W):
        A[i][j] = input()

H = H - 1
W = W - 1
C = 0
for i in range(W):
    for j in range(H):
        if A[i][j] == "*":
            B = A[i][j]
            N = 0
            l = i
            while B != "." and l != 0:
                B = A[l][j]
                N = N + 1
                l = l - 1
            M = 0
            F = 0
            T = 0    
            for k in range(N):
                B = A[i][j+1]
                if B != ".":
                    M = M + 1
            for k in range(N):
                B = A[i][j-1]
                if B != ".":
                    F = F + 1
            for k in range(N+1):
                B = A[i+1][j]
                if B != ".":
                    T = T + 1
            if N == M and N == F:
                if T > N:
                    C = C + 1

print (C)