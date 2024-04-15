t = int(input())
for _ in range(t):
    n = input()
    a = int(n[0]+n[1])
    if a == 0:
        print(f"12:{n[3]}{n[4]} AM")
    elif a == 12:
        print(f"{n} PM")
    elif a > 12:
        a -= 12
        if a < 10:
            a = str(f"0{a}")
        print(f"{a}:{n[3]}{n[4]} PM")
    else:
        print(f"{n} AM")
