n=int(input("digite su entero: "))
a=list(range(1,n))

for i in a:
    if i and n:
        a.append(i**3)
print(a)