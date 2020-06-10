from tkinter import * 
import tkinter.messagebox as msgbox
import webbrowser
from os import getcwd


path = getcwd()
new = 1
ins_url = path + "\inserting.py"
upd_url = path + "\\updating.py"
dlt_url = path + "\deleting.py"
shw_url = path + "\listing.py"

def inserting () : 
	webbrowser.open(ins_url,new=new)
		
def updating () :
	webbrowser.open(upd_url,new=new)

def deleting():
	webbrowser.open(dlt_url,new=new)
def show():
	webbrowser.open(shw_url,new=new)



stu = Tk()
stu.geometry("640x320")
stu.title ("Students's table")
slabel = Label ( stu , text = " Please choose your action " , font = ('bold' , 16))
slabel.place( x = 170 , y = 10 )
List   = Button( stu , text = "List-All" , font = ("italic" , 14 ) , bg = "white" , command = show )
List.place (x = 80 , y = 120)
update = Button( stu , text = "UPDATE" , font = ("italic" , 14 ) , bg = "white" , command = updating )
update.place (x = 200 , y = 120 )
insert = Button( stu , text = "INSERT" , font = ("italic" , 14 ) , bg = "white" , command = inserting )
insert.place (x = 320 , y = 120 )
delete = Button( stu , text = "DELETE" , font = ("italic" , 14 ) , bg = "white" , command = deleting )
delete.place (x = 460 , y = 120 )
stu.mainloop()