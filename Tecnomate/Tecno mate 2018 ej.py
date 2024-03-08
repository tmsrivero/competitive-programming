n = int(input())
k = int(input())

n = 10
def findCapicua():
    #Intervalo inferior
    a= n.len()
    #Intervalo superior 
    b= k
    #Contador para la cantidad de capicuas
    c=0
    print("Los capicuas encontrados son los siguientes:")
    for i in range(a,b+1):
        num_s=str(i)
        num_list=list(num_s)
        if num_list==num_list[::-1]:
            cap=''.join(num_list)
            c+=1
            print(cap)
            
    print("Total de Capicuas:",c)

findCapicua()