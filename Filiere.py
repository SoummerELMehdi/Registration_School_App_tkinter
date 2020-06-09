from tkinter import *

# dir chi BD initialisiha b hado "Statistique - Economie appliquée", "Statistique - Démographie", "Recherche Opérationnelle et Aide à la Décision", "Actuariat - Finance", "Data and Software Engineering"," Data Science")

root = Tk()
root.geometry("600x300")
root.title("Filiere")


filiere = Label(root, text="Ajouter une Filiere",font=("bold",10))
filiere.place(x=25,y=120)

e_filiere = Entry()
e_filiere.place(x=150, y=120)




list=Listbox(root,width=30,height=17)
list.place(x=390, y=10)
# define show methode to show Data base l3ibat

Button(root, text='Submit',width=10,bg='green',fg='white').place(x=50,y=200)

Button(root, text='Modifier',width=10,bg='red',fg='white').place(x=150,y=200)

Button(root, text='Supprimer',width=10,bg='blue',fg='white').place(x=250,y=200)

root.mainloop()