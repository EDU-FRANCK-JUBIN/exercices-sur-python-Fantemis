import random

def valide(sequence_adn):
    if len(sequence_adn) > 0:
        for i, c in enumerate(sequence_adn):
            if c != 'a' and c != 't' and c != 'g' and c != 'c':
                print("invalide.")
                break
    else:
        print("invalide")
def saisie(taille_chaine_adn):
    sequence_adn = []
    for i in range(1, taille_chaine_adn+1):
        valid_char = ['a', 't', 'g', 'c']
        random_valid_char = random.choice(valid_char)
        sequence_adn+=random_valid_char
    print(sequence_adn)

def proportion(chaine, sequence):
    taille_sequence = len(sequence)
    taille_chaine = len(chaine)
    nombre_occurences = len(sequence.split(sequence))
    pourcentage_occurences = ((nombre_occurences)/taille_chaine)*100
    print(pourcentage_occurences)


proportion("attgcaatggtggtacatg", "ca")