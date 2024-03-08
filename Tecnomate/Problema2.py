a = str(input()).upper()
l = len(a)
p = a[0]
c = 1
c2 = 0
q = True
while a != "*":
    for i in range (l-1):
        if a[i] == " ":
            c = c + 1
            c2 = 0
        elif a[i] != " ":
            c2 = c2 + 1
        
        if a[i] == " ":
            if a[i+1] != p:
                q = False
        if c > 50 or c2 > 20:
            q = False
        if q == False:
            break
    if q == False:
        print ("N")
    else:
        print ("Y")
    a = str(input()).upper()
    l = len(a)
    p = a[0]
    c = 1
    c2 = 0
    q = True    
