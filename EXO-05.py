def minMaxMoy(liste_entiers):
    min_max_moy = ()
    min_max_moy += (min(liste_entiers),)
    min_max_moy += (sum(liste_entiers)/len(liste_entiers),)
    min_max_moy += (max(liste_entiers),)

    print(min_max_moy)

minMaxMoy([10, 18, 14, 20, 12, 16])