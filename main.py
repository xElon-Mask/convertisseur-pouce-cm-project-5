pouce = 2.54

cm = 0.394



def conversion(unite):
    input(f"Rentrez la valeur à convertir en {unite}")
   

def conversion_pouce():
    print("a developper")

# 1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

# 2 - Demander à l'utilisateur de rentrer la valeur à convertir (en reprécisant l'unité)


choix_user = input("Souhaitez-vous convertir des pouces en cm, ou des cm en pouces ? Choisissez le numéro correspondant : 1 - Convertir des pouces en cm 2 - Convertir des cm en pouces")
if choix_user == "1":
    conversion("cm")
elif choix_user == "2":
    conversion_pouce("pouces")
else:
    print("ERREUR: Vous ne pouvez rentrer que 1 ou 2")
