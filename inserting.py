from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

"""cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()"""

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

fr = Frame( insert , bg = 'cornsilk4' )
fr.pack()

inf = Label ( fr , text = ' Enter the required informations ' , font = ('arial' , 15 ,'bold' )  , relief = 'solid'  , bg = 'cornsilk3' , fg = 'black' ,bd = 6 )
inf.grid ( row = 0 , column = 0 , columnspan = 2 , pady = 10)

btnframe = Frame ( fr ,width = 100 , height = 100 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

txtframe = Frame ( fr ,width = 100 , height = 100 , relief = 'ridge', bg = 'cornsilk3' , bd = 6 )
txtframe.grid ( row = 1 ,column = 0 , pady = 10 )

var = StringVar(txtframe)
var.set("Statistique - Economie appliquée")
l_s_id = Label(txtframe, text="Enter the student's ID : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_id.grid(row = 0 , column = 0 )
l_s_name = Label(txtframe, text="Student's name : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_name.grid(row = 1 , column = 0)
l_s_prenom = Label(txtframe, text="Student's last name :",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_prenom.grid(row = 2 , column = 0)
l_s_age = Label(txtframe, text="Student's age :",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_age.grid(row = 3 , column = 0)
l_s_filiere = Label (txtframe, text="Student's major : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_filiere.grid(row = 4 , column = 0)
s_filiere = OptionMenu(txtframe, var,"Statistique - Economie appliquée", "Statistique - Démographie", "Recherche Opérationnelle et Aide à la Décision", "Actuariat - Finance", "Data & Software Engineering"," Data Science", command = get_filiere)
s_filiere.config(font=("arial",8,'bold'),bg = 'cornsilk3' , fg = 'black')
s_filiere["menu"].config(font=("arial",8,'bold'),bg = 'cornsilk3' , fg = 'black')
s_filiere.grid(row = 4 , column = 1)
s_id = Entry (txtframe , width = 36)
s_id.grid( row = 0 , column = 1)
s_nom = Entry (txtframe , width = 36)
s_nom.grid(row = 1 , column = 1)
s_prenom = Entry (txtframe , width = 36)
s_prenom.grid(row = 2 , column = 1)
s_age = Entry (txtframe , width = 36)
s_age.grid(row = 3 , column = 1)

btn = Button ( btnframe , text = "INSERT" , font = ("italic" , 20 ) , bg = "cornsilk4", fg = 'cornsilk3' , padx = 120 , pady = 5  , command = insert )
btn.grid(row = 0 , column = 0)
insert.mainloop()