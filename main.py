def info_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " + nom + ", " +
          "vous avez " + str(age) + " ans.")
    print(f"Vous vous appelez {nom}, vous avez {age} ans.")

    print("L'an prochain vous aurez " + str(age+1) + " ans")

    if age == 17:
        print("Vous êtes presque majeur")
    elif 12 <= age < 18:  # age >= 12 and < 18:
        print("Vous êtes adolescents")
    elif age == 1 or age == 2:
        print("Vous êtes bébé")
    elif age == 18:
        print("Vous êtes majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes enfant")
    elif age >= 18:
        print("vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher la taille
    if not taille == 0:
        print("votre taille : " + str(taille) + "m")


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


# nom1 = demander_nom()
# nom2 = demander_nom()

# nom1 = "personne1"
# nom2 = "personne2"

# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# info_personne(nom1, age1)

# info_personne(nom2, age2)

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    info_personne(nom, age, 1.60)
