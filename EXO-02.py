entier_sup_un = int(input("Veuillez entrer un entier supérieur à 1"))
diviseurs = []

for i in range(1, entier_sup_un+1):
    if not entier_sup_un % i:
        diviseurs.append(i)
diviseurs.remove(entier_sup_un)
diviseurs.remove(1)
print(diviseurs)