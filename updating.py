from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()


def updating () : 
	sid = s_id.get()
	nom = s_nom.get()
	prenom = s_prenom.get()
	age = s_age.get()
	fid = s_filiere.get()	
	if ( sid == "" or fid == "" ) :
		msgbox.showinfo (" update Status " , " Missing fields ! " )
	else :
		cur.execute (" update students set idEtudiant = '"+ sid + "',idFiliere ='" + fid + "',nom ='" + nom + "',prenom ='" + prenom + "',age ='" + age + "'" )
		cnct.commit()
		msgbox.showinfo(" update Status ","updated successfully")
		cnct.close()

update = Tk()
update.geometry("640x320")
update.title ( "Updateing" )
l_s_id = Label(update, text="Enter the student's ID : ",font=("bold",10)).grid(row = 0 , column = 0 )
l_s_name = Label(update, text="Student's name : ",font=("bold",10)).grid(row = 1 , column = 0)
l_s_prenom = Label(update, text="Student's last name :",font=("bold",10)).grid(row = 2 , column = 0)
l_s_age = Label(update, text="Student's age :",font=("bold",10)).grid(row = 3 , column = 0)
l_s_filiere = Label (update, text="His major's ID : ",font=("bold",10)).grid(row = 4 , column = 0)
s_id = Entry (update , width = 30)
s_id.grid( row = 0 , column = 2)
s_nom = Entry (update , width = 30)
s_nom.grid(row = 1 , column = 2)
s_prenom = Entry (update , width = 30)
s_prenom.grid(row = 2 , column = 2)
s_age = Entry (update , width = 30)
s_age.grid(row = 3 , column = 2)
s_filiere = Entry (update , width = 30)
s_filiere.grid(row = 4 , column = 2)
btn = Button ( update , text = "update" , font = ("italic" , 20 ) , bg = "white"  , command = updating ).grid(row = 6 , column = 1)
update.mainloop()