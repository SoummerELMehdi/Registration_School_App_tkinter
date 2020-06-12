from tkinter import * 
import tkinter.messagebox as msgbox
import mysql.connector as mysql

"""cnct = mysql.connect( host = "sql7.freemysqlhosting.net" , user = "sql7347048" , password = "tPxP54SNLc" , database = "sql7347048" )
cur = cnct.cursor() """

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
delete.geometry("640x320")
delete.title ( "Deleteing" )
delete.config(bg = 'cornsilk3')
fr = Frame(delete , bg = 'cornsilk4' )
fr.pack()

inf = Label ( fr , text = ' Enter the required informations ' , font = ('arial' , 15 ,'bold' )  , relief = 'solid'  , bg = 'cornsilk3' , fg = 'black' ,bd = 6 )
inf.grid ( row = 0 , column = 0 , columnspan = 3 , pady = 10)

btnframe = Frame ( fr ,width = 40 , height = 40 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

txtframe = Frame ( fr ,width = 40 , height = 40 , relief = 'ridge', bg = 'cornsilk3' , bd = 6 )
txtframe.grid ( row = 1 ,column = 0 , pady = 10 )

l_f_id = Label( txtframe , text = "Enter the major's ID : ",font=("arial",10,'bold') ,  bg = 'cornsilk3' , fg = 'black' )
l_f_id.grid(row = 0 , column = 0 , pady = 5 , padx = 5)

f_id = Entry (txtframe , width = 40)
f_id.grid( row = 0 , column = 1 , padx = 30)

btn = Button ( btnframe , text = "Delete" , font = ("italic" , 15 )  , width = 12 ,bg = "cornsilk4", fg = 'cornsilk3' , padx = 150 , pady = 5 , command = deleting )
btn.grid(row = 0 , column  = 0 , columnspan = 2 )

delete.mainloop()