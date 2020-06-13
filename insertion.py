from tkinter import * 
import tkinter.messagebox as mbox
import sqlite3 


def insert () : 
	Eid = Etudiant_id.get()
	nom = Etudiant_nom.get()
	prenom = Etudiant_prenom.get()
	age = Etudiant_age.get()
	filiere = Etudiant_filiere.get()	
	if ( Eid == "" or nom == "" or prenom == "" or age =="" or filiere == "" ) :
		mbox.showinfo(" Remplisser tous les champs ! " )
	else :
		cnx=sqlite3.connect("App.db")
		cursor=cnx.cursor()
		cursor.execute ("INSERT INTO Etudiant (idEtudiant,IdFiliereFK,nom,prenom,age) VALUES (? ,? ,? ,?,? )" , ( Eid ,filiere,nom,prenom,age) )
		cnx.commit()
		mbox.showinfo("Succes de l'insertion !")
		cnx.close()

insert = Tk()
insert.geometry("359x215")
insert.title ( "Insertion Etudiant" )

fr = Frame( insert , bg = 'LightSteelBlue2' )
fr.pack()

btnframe = Frame ( fr ,width = 100 , height = 150 , relief = 'ridge' , bg = 'LightSteelBlue4' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

textFrame = Frame ( fr ,width = 100 , height = 100 , relief = 'ridge', bg = 'LightSteelBlue4' , bd = 6 )
textFrame.grid ( row = 1 ,column = 0 , pady = 10 )



label_id = Label(textFrame, text="ID Etudiant : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_id.grid(row = 0 , column = 0 )
label_name = Label(textFrame, text="Nom : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_name.grid(row = 1 , column = 0)
label_prenom = Label(textFrame, text="Prenom :",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_prenom.grid(row = 2 , column = 0)
label_age = Label(textFrame, text="Age :",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_age.grid(row = 3 , column = 0)
label_filiere = Label (textFrame, text="Filiere : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_filiere.grid(row = 4 , column = 0)
Etudiant_filiere = Entry(textFrame, width=36)
Etudiant_filiere.grid(row = 4 , column = 1)
Etudiant_id = Entry (textFrame , width = 36)
Etudiant_id.grid( row = 0 , column = 1)
Etudiant_nom = Entry (textFrame , width = 36)
Etudiant_nom.grid(row = 1 , column = 1)
Etudiant_prenom = Entry (textFrame , width = 36)
Etudiant_prenom.grid(row = 2 , column = 1)
Etudiant_age = Entry (textFrame , width = 36)
Etudiant_age.grid(row = 3 , column = 1)

btn = Button ( btnframe , text = "Inserer" , font = ("Arial" , 20 ) , bg = "LightSteelBlue4", fg = 'black' , padx = 120 , pady = 5  , command = insert)
btn.grid(row = 0 , column = 0)
insert.mainloop()