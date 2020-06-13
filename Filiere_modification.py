from tkinter import * 
import tkinter.messagebox as mbox
import sqlite3 

def modifier():
    if(Filiere_id.get()=="" or Filiere_nom.get()=="" ):
        mbox.showinfo("Insert Status", "Tous les champs doivent être remplis")
    else:
        conn=sqlite3.connect('App.db')
        c=conn.cursor()
        c.execute("UPDATE etudiant SET idFiliere=?, nomFiliere=? ",(Filiere_id.get(),Filiere_nom.get(),))
        c.commit()
        
        Filiere_id.delete(0,'end')
        Filiere_nom.delete(0,'end')
        mbox.showinfo("Update succes !")
        conn.close()



modifier = Tk()
modifier.geometry("368x150")
modifier.title ( "Modifier Filiere" )

frame = Frame( modifier , bg = 'LightSteelBlue2' )
frame.pack()

btnframe = Frame ( frame ,width = 100 , height = 150 , relief = 'ridge' , bg = 'LightSteelBlue4' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

textFrame = Frame ( frame ,width = 100 , height = 100 , relief = 'ridge', bg = 'LightSteelBlue4' , bd = 6 )
textFrame.grid ( row = 1 ,column = 0 , pady = 10 )



label_id = Label(textFrame, text="ID Filiere : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_id.grid(row = 0 , column = 0 )
label_name = Label(textFrame, text="Nom Filiere : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_name.grid(row = 1 , column = 0)
Filiere_id = Entry (textFrame , width = 36)
Filiere_id.grid( row = 0 , column = 1)
Filiere_nom = Entry (textFrame , width = 36)
Filiere_nom.grid(row = 1 , column = 1)


btn = Button ( btnframe , text = "Modifier" , font = ("Arial" , 20 ) , bg = "LightSteelBlue4", fg = 'black' , padx = 120 , pady = 5  , command = modifier )
btn.grid(row = 0 , column = 0)

modifier.mainloop()