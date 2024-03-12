t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    an = list(map(int, input().split()))
    am = list(map(int, input().split()))
    an = sorted(an)
    am = sorted(am)

    cont = 0
    for i in range(len(an)):
        for j in range(len(am)):
            if an[i] + am[j] <= k:
                cont += 1
            else:
                break

    print(cont)
