from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()

def deleting () :
	fid = f_id.get()
	if ( fid == "" ) :
		msgbox.showinfo (" Delete Status " , " Missing fields ! " )
	else :
		cur.execute (" DELETE FROM filieres WHERE idFiliere ='" + fid +"'" )
		cnct.commit()
		msgbox.showinfo(" Delete Status ","Deleted successfully")
		cnct.close()

delete = Tk()
delete.geometry("480x144")
delete.title ( "Deleteing" )
l_f_id = Label(delete, text = "Enter the student's ID : ",font=("bold",10)).grid(row = 0 , column = 0 )
f_id = Entry (delete , width = 30)
f_id.grid( row = 0 , column = 1)
btn = Button ( delete , text = "delete" , font = ("italic" , 15 ) , bg = "white"  , command = deleting ).place(x = 340 , y = 1)
delete.mainloop()