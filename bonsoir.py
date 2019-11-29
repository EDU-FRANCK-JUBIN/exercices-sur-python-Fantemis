from easygui import *
msg = "Bonsoir, veullez entrer vos informations"
fieldNames = ["Prenom","Nom","Téléphne","Email"]
meschoix = multenterbox(msg, 'bonsoir', fieldNames)

#pizzas predef
reine = "tomate mozza jambon champi"
diavola = "tomate mozza salami piquant"
sicilienne = "tomate mozza basilic anchois capres champi"
hawaienne = "creme mozza jambon ananas"
capriciosa = "creme mozza champignon artichaut jambon olives huile dolive"
choices = [reine, diavola, sicilienne, hawaienne, capriciosa]

nombrepizza = enterbox("Combien de pizzas chef ?", "Nombre de pizzas")
pizza_custom_yn = ynbox("Voulez-vous faire une pizza custom ?")
print(pizza_custom_yn)
if not pizza_custom_yn:
    choice = choicebox("Choisissez votre pizza", "Choix de la pizza", choices)
    msgbox("Merci " + meschoix[0] + "! Ta commande pour la pizza " + choice + " a bien été enregistrée :)")