N = int (input())
K = int (input()) 
i = 0

while N > 0:
    i = i + 1
    if (N == K) or (N < K):
        N = N - K
    elif (N < (2*K+1)):
        N = N - 2
    elif (N < (2*K)):
        N = N - K
    elif (N == (K+1)):
        N = N - K
    else:
        N = N - K

if ((i%2) == 1):
    print ("Eric")
elif ((i%2) == 0):
    print ("Matias")