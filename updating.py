from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

"""cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()"""


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

fr = Frame( update , bg = 'cornsilk4' )
fr.pack()

inf = Label ( fr , text = ' Enter the required informations ' , font = ('arial' , 15 ,'bold' )  , relief = 'solid'  , bg = 'cornsilk3' , fg = 'black' ,bd = 6 )
inf.grid ( row = 0 , column = 0 , columnspan = 2 , pady = 10)

btnframe = Frame ( fr ,width = 100 , height = 100 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

txtframe = Frame ( fr ,width = 100 , height = 100 , relief = 'ridge', bg = 'cornsilk3' , bd = 6 )
txtframe.grid ( row = 1 ,column = 0 , pady = 10 )

l_s_id = Label(txtframe, text="Enter the student's ID : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_id.grid(row = 0 , column = 0 )
l_s_name = Label(txtframe, text="Student's name : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_name.grid(row = 1 , column = 0)
l_s_prenom = Label(txtframe, text="Student's last name :",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_prenom.grid(row = 2 , column = 0)
l_s_age = Label(txtframe, text="Student's age :",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_age.grid(row = 3 , column = 0)
l_s_filiere = Label (txtframe, text="His major's ID : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black')
l_s_filiere.grid(row = 4 , column = 0)
s_id = Entry (txtframe , width = 30)
s_id.grid( row = 0 , column = 2)
s_nom = Entry (txtframe , width = 30)
s_nom.grid(row = 1 , column = 2)
s_prenom = Entry (txtframe , width = 30)
s_prenom.grid(row = 2 , column = 2)
s_age = Entry (txtframe , width = 30)
s_age.grid(row = 3 , column = 2)
s_filiere = Entry (txtframe , width = 30)
s_filiere.grid(row = 4 , column = 2)
btn = Button ( btnframe , text = "Update" , font = ("italic" , 20 ) ,  bg = "cornsilk4", fg = 'cornsilk3' , padx = 104 , pady = 5 , command = updating )
btn.grid(row = 0 , column = 0)
update.mainloop()