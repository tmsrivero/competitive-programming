t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    print(s.count("map") + s.count("pie") - s.count("mapie"))
