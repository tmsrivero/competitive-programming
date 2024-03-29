import sys

# m is size of coins array (number of
# different coins)


def minCoins(coins, m, V):

    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(V + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]


# Driver Code

coins = [1, 3, 6, 10, 15]
m = len(coins)
t = int(input())
for _ in range(t):
    V = int(input())
    ban = 0

    if (V >= 10**8):
        ban = 1
        V = V-99999990
    elif (V >= 10**7):
        ban = 2
        V = V-9999990
    elif (V >= 10**6):
        ban = 3
        V = V-999990

    print(V)

    if (ban == 0):
        print(int(minCoins(coins, m, V)))
    elif (ban == 1):
        print(int(minCoins(coins, m, V)) + 6666666)
    elif (ban == 2):
        print(int(minCoins(coins, m, V)) + 666666)
    elif (ban == 3):
        print(int(minCoins(coins, m, V)) + 66666)
