from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()


def updating () : 
	fid = f_id.get()
	nom = f_nom.get()	
	if ( fid == "" or nom == "" ) :
		msgbox.showinfo (" update Status " , " Missing fields ! " )
	else :
		cur.execute (" update filieres set nomFiliere ='" + nom + "' WHERE idFiliere = '" + fid +"'" )
		cnct.commit()
		msgbox.showinfo(" update Status ","updated successfully")
		cnct.close()

update = Tk()
update.geometry("450x100")
update.title ( "Updateing" )
l_f_id = Label(update, text="Enter the major's ID : ",font=("bold",10)).grid(row = 0 , column = 0 )
l_f_name = Label(update, text="Major's name : ",font=("bold",10)).grid(row = 1 , column = 0)
f_id = Entry (update , width = 30)
f_id.grid( row = 0 , column = 2)
f_nom = Entry (update , width = 30)
f_nom.grid(row = 1 , column = 2)
btn = Button ( update , text = "update" , font = ("italic" , 15 ) , bg = "white"  , command = updating ).place(x = 340 , y = 1)
update.mainloop()