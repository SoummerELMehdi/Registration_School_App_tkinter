from tkinter import *
import tkinter.messagebox as messagebox
import webbrowser
import sqlite3 


root = Tk()
root.geometry("530x330")
root.title("Filiere ")

new = 1

def show():
    cnx=sqlite3.connect('App.db')
    cursor=cnx.cursor()
    cursor.execute("SELECT * FROM Filiere")
    rows=cursor.fetchall()
    listF.delete(0, listF.size())

    for row in rows:
        Data=row[0]+"    "+row[1]+"    "+row[2]+"    "+row[3]+"    "+row[4]
        listF.insert(listF.size()+1,Data)
    cnx.close()


def InsererF () : 
	exec(open("Filiere_insertion.py").read())

def ModifierF () :
	exec(open("Filiere_modification.py").read())

def SupprimerF ():
	exec(open("Filiere_supprimer.py").read())



listF=Listbox(root,width=85,height=15)
listF.place(x=10, y=10)

mainframe = Frame( root)
mainframe.place(x=115,y=260)


frame1 = Frame ( mainframe ,width = 10 , height = 10 , relief = 'ridge' , bg = 'LightSkyBlue1' , bd = 4 )
frame1.grid( row = 0 , column = 1 ,pady = 3)
frame2 = Frame ( mainframe ,width = 10 , height = 10 , relief = 'ridge' , bg = 'LightSkyBlue1' , bd = 4 )
frame2.grid( row = 0 , column = 2 ,pady = 3)
frame3 = Frame ( mainframe ,width = 10 , height = 10 , relief = 'ridge' , bg = 'LightSkyBlue1' , bd = 4 )
frame3.grid( row = 0 , column = 3 ,pady = 3)

Btn1 = Button(frame1, text = "Inserer",font = ("Arial" , 10 ),bg="LightSteelBlue4", pady = 10,padx = 15 ,command=InsererF)
Btn1.grid (row = 0 , column = 0 , rowspan = 1 )
Btn2 = Button(frame2, text = "Modifier",font = ("Arial" , 10 ),bg="LightSteelBlue4", pady = 10,padx = 15,command=ModifierF)
Btn2.grid (row = 0 , column = 2 , rowspan = 1)
Btn3 = Button(frame3, text = "Supprimer",font = ("Arial" , 10 ),bg="LightSteelBlue4", pady = 10,padx = 15,command=SupprimerF)
Btn3.grid (row = 0 , column = 4 , rowspan = 1)

show()
root.mainloop()

