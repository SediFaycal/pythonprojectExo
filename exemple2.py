import tkinter as tk

def inscription():
    pseudo = pseudo_entry.get()
    mot_de_passe = mot_de_passe_entry.get()
    email = email_entry.get()
    
    print(f"Pseudo : {pseudo}")
    print(f"Mot de passe : {mot_de_passe}")
    print(f"Email : {email}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Inscription")
#dimension fenetre
fenetre.geometry("400x300")

# Création des labels et des placeholder de saisie
pseudo_label = tk.Label(fenetre, text="Pseudo:")
pseudo_label.pack()
pseudo_entry = tk.Entry(fenetre)
pseudo_entry.pack()

mot_de_passe_label = tk.Label(fenetre, text="Mot de passe:")
mot_de_passe_label.pack()
mot_de_passe_entry = tk.Entry(fenetre, show="*")  # Pour masquer le mot de passe
mot_de_passe_entry.pack()

email_label = tk.Label(fenetre, text="Email:")
email_label.pack()
email_entry = tk.Entry(fenetre)
email_entry.pack()

# Bouton d'inscription
inscription_button = tk.Button(fenetre, text="Inscription", command=inscription)
inscription_button.pack()

# Lancement de la boucle principale de l'interface graphique
fenetre.mainloop()


# def action_bouton():
#     print("le bouton a été cliquez !")

# fenetre = tk.Tk()
# #nom de la fenetre
# fenetre.title("ma premiere interface")

# #afficher un texte 
# etiquette = tk.Label(fenetre, text="Bravo tu as fais ta premiere interface graphique")
# #afficher etiquette
# etiquette.pack()

# #bouton
# bouton = tk.Button(fenetre, text="cliquez sur moi !", command=action_bouton)
# bouton.pack()

# #dimension fenetre
# fenetre.geometry("400x300")

# #ne se ferme pas 
# fenetre.mainloop()