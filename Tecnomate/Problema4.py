N = int(input())
for i in range (N):
    A = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for k in range (9):
        for j in range (9):
            A[k][j] = int(input())
    q = True
    c = 0
    while q == True and c < 9:
        for k in range (9):
            for j in range(9):
                if k != j:
                    if A[c][k] == A[c][j]:
                        q = False
        c = c+1
    c = 0
    while q == True and c < 9:
        for k in range (9):
            for j in range (9):
                if k != j:
                    if A[k][c] == A[j][c]:
                        q = False
        c = c+1
    print ("Instancia", i+1)
    if q == True:
        print ("SIM")
    else:
        print ("NAO")
    print ("")