from tkinter import *
import webbrowser

root = Tk()

new = 1
url1 = "Etudiant.py"
url2 = "Filiere.py"
def openurl1():
    webbrowser.open(url1,new=new)

def openurl2():
    webbrowser.open(url2,new=new)

BtnE = Button(root, text = "Etudiant",bg="green",command=openurl1)
BtnE.pack(side = LEFT)
BtnE.place(x=30,y=60)
BtnF = Button(root, text = "Filiere",bg="green",command=openurl2)
BtnF.pack( side = LEFT)
BtnF.place(x=130,y=60)


root.mainloop()