"""
1 pouce = 2,54cm
1 cm = 0,394 pouces
"""

"""
effectuer_conversion : Cette fonction convertit les unités unit1 vers unit2

Return :
True : L'utilisateur ne veut plus convertir
False : L'utilisateur a donné une valeur à convertir
"""

# Conversion de unit1 vers unit2
def effectuer_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False

print("Ce programme vous permet d'effectuer des conversions d'unités")
print("1 - Pouces vers cm")
print("2 - cm vers pouces")
choice = input("Votre choix (1 ou 2): ")
if choice == "1":
    effectuer_conversion("pouces", "cm", 2.54)
if choice == "2":
    effectuer_conversion("cm", "pouces", 0.394)


"""
if effectuer_conversion("pouces", "cm", 2.54) == True, alors on sort de la boucle avec break car la fonction renvoie True lorsque
l'utilisateur à rentrer q pour quitter. En python le paramètre par défaut est True, donc pas besoin de le préciser pour la condition du if
"""
while True:
    if choice == "1":
        if effectuer_conversion("pouces", "cm", 2.54):
            break
    if choice == "2":
        if effectuer_conversion("cm", "pouces", 0.394):
            break