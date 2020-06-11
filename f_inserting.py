from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()

def inserting () : 
	fid = f_id.get()
	nom = f_nom.get()	
	if ( fid == "" ) :
		msgbox.showinfo (" Insert Status " , " Missing fields ! " )
	else :
		cur.execute (" INSERT INTO filieres VALUES (%s,%s) " , ( fid ,nom) )
		cnct.commit()
		msgbox.showinfo(" Insert Status ","Inserted successfully")
		cnct.close()

insert = Tk()
insert.geometry("450x100")
insert.title ( "Inserting" )
l_f_id = Label(insert, text="Enter the major's ID : ",font=("bold",10)).grid(row = 0 , column = 0 )
l_f_name = Label(insert, text="Major's name : ",font=("bold",10)).grid(row = 1 , column = 0)
f_id = Entry (insert , width = 30)
f_id.grid( row = 0 , column = 2)
f_nom = Entry (insert , width = 30)
f_nom.grid(row = 1 , column = 2)
btn = Button ( insert , text = "INSERT" , font = ("italic" , 15 ) , bg = "white" , command = inserting )
btn.place(x = 340 , y = 1)
insert.mainloop()