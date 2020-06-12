from tkinter import * 
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
stu.geometry("400x540")
stu.title ("Students's table")

mainframe = Frame( stu , bg = 'cornsilk4' )
mainframe.pack()

slabel = Label ( mainframe , text = " Please choose your action " , relief = 'solid' , font = ('arial' , 15 ,'bold' )  , bg = 'cornsilk3' , fg = 'black' ,bd = 6 )
slabel.grid ( row = 0 , column = 0  , pady = 20)

btn_1_frame = Frame ( mainframe ,width = 40 , height = 40 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btn_1_frame.grid( row = 1 , column = 0 ,pady = 5)
btn_2_frame = Frame ( mainframe ,width = 40 , height = 40 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btn_2_frame.grid( row = 2 , column = 0 ,pady = 5)
btn_3_frame = Frame ( mainframe ,width = 40 , height = 40 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btn_3_frame.grid( row = 3 , column = 0 ,pady = 5)
btn_4_frame = Frame ( mainframe ,width = 40 , height = 40 , relief = 'ridge' , bg = 'cornsilk3' , bd = 6 )
btn_4_frame.grid( row = 4 , column = 0 ,pady = 5)



List   = Button( btn_1_frame , text = "List-All" , font = ("italic" , 14 ) , bg = "cornsilk4" , fg = 'cornsilk3',pady = 10,padx = 20 , command = show )
List.grid (row = 0 , column = 0 , columnspan = 2 )
update = Button( btn_2_frame , text = "UPDATE" , font = ("italic" , 14 ) , bg = "cornsilk4" , fg = 'cornsilk3',pady = 10,padx = 10 , command = updating )
update.grid (row = 0 , column = 0 , columnspan = 2)
insert = Button( btn_3_frame , text = "INSERT" , font = ("italic" , 14 ) , bg = "cornsilk4" , fg = 'cornsilk3',pady = 10,padx = 13 , command = inserting )
insert.grid (row = 0 , column = 0 , columnspan = 2)
delete = Button( btn_4_frame , text = "DELETE" , font = ("italic" , 14 ) , bg = "cornsilk4", fg = 'cornsilk3' ,pady = 10,padx = 11 , command = deleting )
delete.grid (row = 0 , column = 0 , columnspan = 2)
stu.mainloop()