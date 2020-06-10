from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()

def deleting () :
	sid = s_id.get()
	if ( sid == "" ) :
		msgbox.showinfo (" Delete Status " , " Missing fields ! " )
	else :
		cur.execute (" DELETE FROM students WHERE idEtudiant = (%s) " , ( sid ) )
		cnct.commit()
		msgbox.showinfo(" Delete Status ","Deleted successfully")
		cnct.close()

delete = Tk()
delete.geometry("480x144")
delete.title ( "Deleteing" )
l_s_id = Label(delete, text = "Enter the student's ID : ",font=("bold",10)).grid(row = 0 , column = 0 )
s_id = Entry (delete , width = 30)
s_id.grid( row = 0 , column = 1)
btn = Button ( delete , text = "delete" , font = ("italic" , 20 ) , bg = "white"  , command = deleting ).grid(row = 0 , column = 2)
delete.mainloop()