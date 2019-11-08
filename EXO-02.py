entier_sup_un = int(input("Veuillez entrer un entier supérieur à 1"))
diviseurs = []

if(entier_sup_un > 1):
    for i in range(1, entier_sup_un+1):
        if not entier_sup_un % i:
            diviseurs.append(i)
    diviseurs.remove(entier_sup_un)
    diviseurs.remove(1)
if(len(diviseurs) == 0):
    print("Il est premier")
print(diviseurs)