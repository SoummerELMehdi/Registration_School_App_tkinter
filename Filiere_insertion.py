from tkinter import * 
import tkinter.messagebox as mbox
import sqlite3 


def insert () : 
	Fid = Filiere_id.get()
	Fnom = Filiere_nom.get()
	
	if ( Fid == "" or Fnom == "" ) :
		mbox.showinfo(" Remplisser tous les champs ! " )
	else :
		cnx=sqlite3.connect("App.db")
		cursor=cnx.cursor()
		cursor.execute ("INSERT INTO Filere (idFiliere, nomFiliere) VALUES (? ,? ,? ,?,? )" , ( Fid,Fnom) )
		cnx.commit()
		mbox.showinfo("Succes de l'insertion !")
		cnx.close()

insert = Tk()
insert.geometry("359x150")
insert.title ( "Insertion Filiere" )

fr = Frame( insert , bg = 'LightSteelBlue2' )
fr.pack()

btnframe = Frame ( fr ,width = 100 , height = 150 , relief = 'ridge' , bg = 'LightSteelBlue4' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

textFrame = Frame ( fr ,width = 100 , height = 100 , relief = 'ridge', bg = 'LightSteelBlue4' , bd = 6 )
textFrame.grid ( row = 1 ,column = 0 , pady = 10 )



label_id = Label(textFrame, text="ID Filiere : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_id.grid(row = 0 , column = 0 )
label_nom = Label(textFrame, text="Nom Filiere : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_nom.grid(row = 1 , column = 0)

Filiere_id = Entry (textFrame , width = 36)
Filiere_id.grid( row = 0 , column = 1)
Filiere_nom = Entry (textFrame , width = 36)
Filiere_nom.grid(row = 1 , column = 1)

btn = Button ( btnframe , text = "Inserer" , font = ("Arial" , 20 ) , bg = "LightSteelBlue4", fg = 'black' , padx = 120 , pady = 5  , command = insert)
btn.grid(row = 0 , column = 0)
insert.mainloop()