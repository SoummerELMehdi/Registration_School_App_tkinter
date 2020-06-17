from tkinter import *
import webbrowser
import sqlite3

root = Tk()
root.geometry("225x75")
root.title("Project App")

def createdb():
    try:
        conn = sqlite3.connect('App.db')
        cursor = conn.cursor()
        cursor.execute('''create table Etudiant (
            idEtudiant  INT  NOT NULL PRIMARY KEY,
            IdFiliereFK INT not null ,
            nom VARCHAR(50) NOT NULL , 
            prenom VARCHAR(50) NOT NULL, 
            age INT NOT NULL)''')
        conn.commit()
        cursor.execute('''create table Filiere (
            idFiliere INT   NOT NULL PRIMARY KEY, 
            nomFiliere  VARCHAR(255) NOT NULL)''')

        conn.commit()
        conn.close()
        print("Database is created")
    except Exception :
        print("Existing database")
createdb()



new = 1
url1 = "Etudiant.py"
url2 = "Filiere.py"
def openurl1():
    exec(open("url1").read())

def openurl2():
    exec(open("url2").read())

mainframe = Frame( root , bg = 'SteelBlue1' )
mainframe.pack()


frame1 = Frame ( mainframe ,width = 30 , height = 30 , relief = 'ridge' , bg = 'LightSkyBlue1' , bd = 4 )
frame1.grid( row = 0 , column = 1 ,pady = 4)
frame2 = Frame ( mainframe ,width = 30 , height = 30 , relief = 'ridge' , bg = 'LightSkyBlue1' , bd = 4 )
frame2.grid( row = 0 , column = 2 ,pady = 4)


BtnE = Button(frame1, text = "Etudiant",font = ("Arial" , 16 ),bg="LightSteelBlue4", pady = 10,padx = 5 ,command=openurl1)
BtnE.grid (row = 0 , column = 0 , rowspan = 1 )
BtnF = Button(frame2, text = "Filiere",font = ("Arial" , 16 ),bg="LightSteelBlue4", pady = 10,padx = 15,command=openurl2)
BtnF.grid (row = 0 , column = 2 , rowspan = 1)


root.mainloop()
