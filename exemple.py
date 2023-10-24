#exo 1 fruits

nom = input("Entrez votre nom : ")
nom = nom.upper()
prenom = input("Entrez votre prénom : ")

taille = input("quelle est votre taille (en centimetre svp) ?")
age = input("Entrez votre âge : ")


fruits = input("Entrez vos fruits préférés (séparés par des virgules ou pas) : ")


info_user = f"Bonjour {prenom} {nom} ! Vous avez {age} ans et vous mesurez {taille} centimetres et vos fruits préférés sont les {fruits}."


print(info_user)