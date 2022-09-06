# 1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

# 2 - Demander à l'utilisateur de rentrer la valeur à convertir (en reprécisant l'unité)

# 3 - Afficher la valeur convertie (et l'unité : cm ou pouces)



pouce_en_cm = 2.54

cm_en_pouce = 0.394



def conversion(unite):
    value_str = input(f"Rentrez la valeur à convertir en {unite}")
    value_int = int(value_str)
    if unite == "cm":
        value_convert_cm = value_int * pouce_en_cm
        return print("Cela donne " + str(value_convert_cm) + f" {unite}")
    else:
        value_convert_pouce = value_int * cm_en_pouce
        return print("Cela donne " + str(value_convert_pouce) + f" {unite}")

   


choix_user = input("Souhaitez-vous convertir des pouces en cm, ou des cm en pouces ? Choisissez le numéro correspondant : 1 - Convertir des pouces en cm 2 - Convertir des cm en pouces")
if choix_user == "1":
    conversion("cm")
elif choix_user == "2":
    conversion_pouce("pouces")
else:
    print("ERREUR: Vous ne pouvez rentrer que 1 ou 2")

print("Fin du programme")