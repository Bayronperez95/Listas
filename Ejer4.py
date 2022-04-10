list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_2=[]
f=0
while f<=5:
    primero=int(input("digite un numero de la lista: "))
    while primero<0:
        print("numero no valido digite numeros positivos: ")
        break
    list_2.append(primero)
    f+=1
    for m in list_2:
        if m <0:
            list_2.remove(primero)
print(list_2)