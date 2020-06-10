from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()

def get_filiere(selection) : 
	global filiere
	filiere = selection
	
def insert () : 
	sid = s_id.get()
	nom = s_nom.get()
	prenom = s_prenom.get()
	age = s_age.get()	
	if ( sid == "" or filiere == "" ) :
		msgbox.showinfo (" Insert Status " , " Missing fields ! " )
	else :
		cur.execute (" INSERT INTO students VALUES (%s,%s,%s,%s,%s) " , ( sid ,filiere,nom,prenom,age) )
		cnct.commit()
		msgbox.showinfo(" Insert Status ","Inserted successfully")
		cnct.close()

insert = Tk()
insert.geometry("640x320")
insert.title ( "Inserting" )
var = StringVar(insert)
var.set("Statistique - Economie appliquée")
l_s_id = Label(insert, text="Enter the student's ID : ",font=("bold",10)).grid(row = 0 , column = 0 )
l_s_name = Label(insert, text="Student's name : ",font=("bold",10)).grid(row = 1 , column = 0)
l_s_prenom = Label(insert, text="Student's last name :",font=("bold",10)).grid(row = 2 , column = 0)
l_s_age = Label(insert, text="Student's age :",font=("bold",10)).grid(row = 3 , column = 0)
l_s_filiere = Label (insert, text="Student's major : ",font=("bold",10)).grid(row = 4 , column = 0)
s_filiere = OptionMenu(insert, var,"Statistique - Economie appliquée", "Statistique - Démographie", "Recherche Opérationnelle et Aide à la Décision", "Actuariat - Finance", "Data & Software Engineering"," Data Science",command = get_filiere)
s_filiere.grid(row = 4 , column = 2)
s_id = Entry (insert , width = 30)
s_id.grid( row = 0 , column = 2)
s_nom = Entry (insert , width = 30)
s_nom.grid(row = 1 , column = 2)
s_prenom = Entry (insert , width = 30)
s_prenom.grid(row = 2 , column = 2)
s_age = Entry (insert , width = 30)
s_age.grid(row = 3 , column = 2)
btn = Button ( insert , text = "INSERT" , font = ("italic" , 20 ) , bg = "white"  , command = insert ).grid(row = 6 , column = 1)
insert.mainloop()