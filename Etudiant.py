from tkinter import *
import tkinter.messagebox as messagebox
#dir BD dyalk o les methodes 
# define show methode to show Data base l3ibat

root = Tk()
root.geometry("600x300")
root.title("Etudiant ")

var = StringVar(root)
var.set("Statistique - Economie appliquée")

id = Label(root, text="Entrer votre ID",font=("bold",10))
id.place(x=20,y=30)

nom = Label(root, text="Entrer votre Nom",font=("bold",10))
nom.place(x=20,y=60)

prenom = Label(root, text="Entrer votre Prenom",font=("bold",10))
prenom.place(x=20,y=90)

filiere = Label(root, text="Entrer votre Filiere",font=("bold",10))
filiere.place(x=25,y=120)

e_id = Entry()
e_id.place(x=150, y=30)

e_nom = Entry()
e_nom.place(x=150, y=60)

e_prenom = Entry()
e_prenom.place(x=150, y=90)

e_filiere = OptionMenu(root, var,"Statistique - Economie appliquée", "Statistique - Démographie", "Recherche Opérationnelle et Aide à la Décision", "Actuariat - Finance", "Data and Software Engineering"," Data Science")
e_filiere.place(x=150, y=120)

list=Listbox(root,width=30,height=17)
list.place(x=390, y=10)


Button(root, text='Submit',width=10,bg='green',fg='white').place(x=50,y=200)

Button(root, text='Modifier',width=10,bg='red',fg='white').place(x=150,y=200)

Button(root, text='Supprimer',width=10,bg='blue',fg='white').place(x=250,y=200)

root.mainloop()

