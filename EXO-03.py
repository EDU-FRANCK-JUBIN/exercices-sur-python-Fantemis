import math
nombre_sup_cinquante = int(input("Veuillez entrer un nombre superieur à 50"))
e = 1
list = []
if(nombre_sup_cinquante > 50):
    for i in range(1, nombre_sup_cinquante + 1):
        e += float(1 / math.factorial(i))
    list.append(e)
    list.append(2.71828182845904523536 - e)
    print(list)
else:
    print("Nombre invalide, relanceez le preogramme")
