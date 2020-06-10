from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()

def show() : 
	cur.execute (" SELECT * FROM students " , ( sid ) )
	rows = cur.fetchall()
	for row in rows : 
		for e in row : 
			data = e +'\t'
		lists.insert(lists.size()+1 ,data )
	cnct.close()
		
		
show = Tk()
show.geometry("480x320")
show.title ( "Showing" )
lists = Listbox(show)
lists.place(relx = 0.5 , rely = 0.5 , anchor = CENTER , height = 300 , width = 300 )
show()
show.mainloop()