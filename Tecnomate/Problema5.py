total = 151
n = int(input())
poke = []
for i in range(n):
    s = input().upper()
    if s in poke:
        0
    else:
        poke.append(s)
        total = total - 1

print("Falta(m)", total, "pomekon(s)")