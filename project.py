import tkinter
import tkinter.messagebox
from tkinter import ttk
import numpy as np
import parserr






#############################################################
window=tkinter.Tk()
window.geometry('800x600')
window.title("Solving system of linear equation")
#######################
ls=tkinter.Label(window,text="Enter the equations",font=('Arial Bold',25))
ls.pack()
ls.place(x=0,y=0)
###############################
txt=tkinter.Text(window,width=25,height=5)
txt.pack()
txt.place(x = 0,y = 45)

##########################################
systems=ttk.Combobox(window)
systems.place(x=210,y=50)
systems['values']=("Gauss Elimination","Gauss Jordan","LU Decomposition","Gauss Seidil","Jacobi Iteration")
systems.current(0)
#####################

################################################
systems1=ttk.Combobox(window)
systems1.place(x=210,y=70)
systems1['values']=("Downlittle Form","Crout Form","Cholesky Form")
systems1.current(0)
#########################################################
lsI=tkinter.Label(window,text="Initials",font=('Arial Bold',15))
lsI.pack()
lsI.place(x=210,y=110)
###########################
txtI=tkinter.Entry(window,width=50)
txtI.place(x = 210,
        y = 140,
        width=150,
        height=20)
######################################################
lsS1=tkinter.Label(window,text="stopping conditions:number of iteration",font=('Arial Bold',15))
lsS1.pack()
lsS1.place(x=210,y=210)        
##################

txt1=tkinter.Entry(window,width=50)
txt1.place(x = 210, y = 240,width=150,height=20)

##################################################################
lsS2=tkinter.Label(window,text="stopping conditions:Error",font=('Arial Bold',15))
lsS2.pack()
lsS2.place(x=210,y=290)               
##################################

txt2=tkinter.Entry(window,width=50)
txt2.place(x = 210,y = 330,width=150,height=20)

#########################################################
def solve():
   es=txt.get("1.0","end-1c")
   es=es.strip()
   obj=parserr.getLists()
   obj.parsing(es+"\n")
   tkinter.messagebox.showinfo( "Hello Python",es[-1])

B = tkinter.Button(window, text ="solve", command = solve)
B.pack()



confirm = tkinter.Button(window, text ="confirm methode")
confirm.pack()
confirm.place(x = 360,y = 49)
window.mainloop

