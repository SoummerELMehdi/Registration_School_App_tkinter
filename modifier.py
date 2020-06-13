from tkinter import * 
import tkinter.messagebox as mbox
import sqlite3 

def modifier():
    if(Etudiant_id.get()=="" or Etudiant_nom.get()=="" or Etudiant_prenom.get()=="" or Etudiant_age.get()=="" or Etudiant_filiere.get()==""):
        mbox.showinfo("Insert Status", "Tous les champs doivent être remplis")
    else:
        conn=sqlite3.connect('App.db')
        c=conn.cursor()
        c.execute("UPDATE etudiant SET nom=?, prenom=?, age=?, IdFiliereFK=? WHERE idEtudiant=?",(Etudiant_nom.get(),Etudiant_prenom.get(),Etudiant_age.get(),Etudiant_filiere.get(),Etudiant_id.get(),))
        c.commit()
        
        Etudiant_id.delete(0,'end')
        Etudiant_nom.delete(0,'end')
        Etudiant_prenom.delete(0,'end')
        Etudiant_age.delete(0,'end')
        Etudiant_filiere.delete(0,'end')
        mbox.showinfo("Update succes !")
        conn.close()



modifier = Tk()
modifier.geometry("368x215")
modifier.title ( "Modifier Etudiant" )

frame = Frame( modifier , bg = 'LightSteelBlue2' )
frame.pack()

btnframe = Frame ( frame ,width = 100 , height = 150 , relief = 'ridge' , bg = 'LightSteelBlue4' , bd = 6 )
btnframe.grid( row = 2 , column = 0 )

textFrame = Frame ( frame ,width = 100 , height = 100 , relief = 'ridge', bg = 'LightSteelBlue4' , bd = 6 )
textFrame.grid ( row = 1 ,column = 0 , pady = 10 )



label_id = Label(textFrame, text="ID Etudiant : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_id.grid(row = 0 , column = 0 )
label_name = Label(textFrame, text="Nom : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_name.grid(row = 1 , column = 0)
label_prenom = Label(textFrame, text="Prenom :",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_prenom.grid(row = 2 , column = 0)
label_age = Label(textFrame, text="Age :",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_age.grid(row = 3 , column = 0)
label_filiere = Label (textFrame, text="Filiere : ",font=("arial",10,'bold') ,  bg = 'LightSteelBlue4' , fg = 'black')
label_filiere.grid(row = 4 , column = 0)
Etudiant_filiere = Entry(textFrame, width=36)
Etudiant_filiere.grid(row = 4 , column = 1)
Etudiant_id = Entry (textFrame , width = 36)
Etudiant_id.grid( row = 0 , column = 1)
Etudiant_nom = Entry (textFrame , width = 36)
Etudiant_nom.grid(row = 1 , column = 1)
Etudiant_prenom = Entry (textFrame , width = 36)
Etudiant_prenom.grid(row = 2 , column = 1)
Etudiant_age = Entry (textFrame , width = 36)
Etudiant_age.grid(row = 3 , column = 1)

btn = Button ( btnframe , text = "Modifier" , font = ("Arial" , 20 ) , bg = "LightSteelBlue4", fg = 'black' , padx = 120 , pady = 5  , command = modifier )
btn.grid(row = 0 , column = 0)

modifier.mainloop()