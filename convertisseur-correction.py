"""
1 pouce = 2,54cm
1 cm = 0,394 pouces
"""

"""
demander_et_afficher_conversion : Cette fonction convertit les unités unit1 vers unit2

Return :
True : L'utilisateur ne veut plus convertir (sortir du programme)
False : L'utilisateur a donné une valeur à convertir
"""
def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        """
        ici on utilise la récursion, on rappelle donc la même fonction pour
        que l'user puisse sortir de l'erreur et retenter sa conversion avec des données
        correctes
        """
        return demander_et_afficher_conversion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False


while True:
    # Menu : choix de la conversion
    print("Ce programme vous permet d'afficher des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choice = input("Votre choix (1 ou 2): ")
    if choice == "1" or choice == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")
 


"""
if demander_et_afficher_conversion("pouces", "cm", 2.54) == True, alors on sort de la boucle avec break car la fonction renvoie True lorsque
l'utilisateur à rentrer q pour quitter. En python le paramètre par défaut est True, donc pas besoin de le préciser pour la condition du if
"""
while True:
    # Demander les valeurs à convertir à l'utilisateur
    if choice == "1":
        if demander_et_afficher_conversion("pouces", "cm", 2.54):
            break
    if choice == "2":
        if demander_et_afficher_conversion("cm", "pouces", 0.394):
            break