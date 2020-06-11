from tkinter import * 
import webbrowser
from os import getcwd


path = getcwd()
new = 1
ins_url = path + "\f_inserting.py"
upd_url = path + "\\f_updating.py"
dlt_url = path + "\f_deleting.py"
shw_url = path + "\f_listing.py"

def inserting () : 
	webbrowser.open(ins_url,new=new)
		
def updating () :
	webbrowser.open(upd_url,new=new)

def deleting():
	webbrowser.open(dlt_url,new=new)
def show():
	webbrowser.open(shw_url,new=new)



stu = Tk()
stu.geometry("270x320")
stu.title ("Major's table")
slabel = Label ( stu , text = " Please choose your action " , font = ('bold' , 16))
slabel.grid( row = 0 )
List   = Button( stu , text = "List-All" , font = ("italic" , 14 ) , bg = "white" ,pady = 10,padx = 20 , command = show )
List.grid (row = 1)
update = Button( stu , text = "UPDATE" , font = ("italic" , 14 ) , bg = "white" ,pady = 10,padx = 10 , command = updating )
update.grid (row = 2)
insert = Button( stu , text = "INSERT" , font = ("italic" , 14 ) , bg = "white" ,pady = 10,padx = 13 , command = inserting )
insert.grid (row = 3 )
delete = Button( stu , text = "DELETE" , font = ("italic" , 14 ) , bg = "white" ,pady = 10,padx = 11 , command = deleting )
delete.grid (row = 4 )
stu.mainloop()