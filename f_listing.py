from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()

def showing() : 
	cur.execute (" SELECT * FROM filieres "  )
	rows = cur.fetchall()
	for row in rows : 
		data = str(row [0]) + "       " +  row [1]
		lists.insert( lists.size()+1 , data )
	cnct.close()
		
		
show = Tk()
show.geometry("480x320")
show.title ( "Showing" )
lists = Listbox(show)
lists.place(relx = 0.5 , rely = 0.5 , anchor = CENTER , height = 310 , width = 470 )
showing()
show.mainloop()