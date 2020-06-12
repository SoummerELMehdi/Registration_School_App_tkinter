from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

"""cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor()
"""
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
insert.geometry("450x240")
insert.title ( "Inserting" )

fr = Frame( insert , bg = 'cornsilk4' )
fr.pack()

inf = Label ( fr , text = ' Enter the required informations ' , font = ('arial' , 15 ,'bold' )  , relief = 'solid'  , bg = 'cornsilk3' , fg = 'black' ,bd = 6 )
inf.grid ( row = 0 , column = 0 , columnspan = 3 , pady = 10)

btnframe = Frame ( fr ,width = 40 , height = 40 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

txtframe = Frame ( fr ,width = 40 , height = 40 , relief = 'ridge', bg = 'cornsilk3' , bd = 6 )
txtframe.grid ( row = 1 ,column = 0 , pady = 10 )

l_f_id = Label(txtframe, text="Enter the major's ID : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black' )
l_f_id.grid(row = 0 , column = 0 )
l_f_name = Label(txtframe, text="Major's name : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black' )
l_f_name.grid(row = 1 , column = 0)
f_id = Entry (txtframe , width = 30)
f_id.grid( row = 0 , column = 2)
f_nom = Entry (txtframe , width = 30)
f_nom.grid(row = 1 , column = 2)
btn = Button ( btnframe , text = "Insert" , font = ("italic" , 15 ) , bg = "cornsilk4", fg = 'cornsilk3' , padx = 120 , pady = 5 , command = inserting )
btn.grid( row = 0  , column = 0 , columnspan = 2 )
insert.mainloop()