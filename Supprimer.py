from tkinter import *
import tkinter.messagebox as mbox
import sqlite3 

def supprimer():

    if(Etudiant_id.get()==""):
        mbox.showinfo("Entrer Id Etudiant !")
    else:
        conn=sqlite3.connect('App.db')
        c=conn.cursor()
        c.execute("DELETE FROM etudiant WHERE idEtudiant=?",(Etudiant_id.get(),))
        conn.commit()

        mbox.showinfo("Delete Status", "Etudiant supprimé")
        conn.close()

modifier = Tk()
modifier.geometry("368x130")
modifier.title ( "Supprimer Etudiant" )

frame = Frame( modifier , bg = 'LightSteelBlue2' )
frame.pack()

btnframe = Frame ( frame ,width = 100 , height = 150 , relief = 'ridge' , bg = 'LightSteelBlue4' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

textFrame = Frame ( frame ,width = 100 , height = 100 , relief = 'ridge', bg = 'LightSteelBlue4' , bd = 6 )
textFrame.grid ( row = 1 ,column = 0 , pady = 10 )



label_id = Label(textFrame, text="ID Etudiant : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_id.grid(row = 0 , column = 0 )


Etudiant_id = Entry (textFrame , width = 36)
Etudiant_id.grid( row = 0 , column = 1)


btn = Button ( btnframe , text = "Modifier" , font = ("Arial" , 20 ) , bg = "LightSteelBlue4", fg = 'black' , padx = 120 , pady = 5  , command = modifier )
btn.grid(row = 0 , column = 0)

modifier.mainloop()