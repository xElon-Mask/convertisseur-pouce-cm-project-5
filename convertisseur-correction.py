"""
1 pouce = 2,54cm
"""

print("Ce programme vous permet d'effectuer des conversions d'unités")
print("1 - Pouces vers cm")
print("2 - cm vers pouces")
choice = input("Votre choix (1 ou 2): ")
if choice == "1":
    valeur_str = input("Conversion Pouces -> cm. Donnez la valeur en pouces : ")
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float * 2.54, 2)
    print(f"Résultat de la conversion : {valeur_float} pouces = {valeur_convertie} cm")
if choice == "2":
    valeur_str = input("Conversion cm -> pouces. Donnez la valeur en cm : ")
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float / 2.54, 2)
    print(f"Résultat de la conversion : {valeur_float} cm = {valeur_convertie} pouces")