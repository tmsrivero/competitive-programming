t = int(input())

for i in range(t):
    n = int(input())
    melody = input()

    melodies = set()
    count = 0

    for i in range(n-1):
        two_notes = melody[i:i+2]

        if two_notes not in melodies:
            melodies.add(two_notes)
            count += 1
    
    print(count)