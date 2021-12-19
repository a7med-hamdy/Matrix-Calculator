### this is the imports
import tkinter
from tkinter.constants import X
import tkinter.messagebox
from tkinter import ttk
import numpy as np
from Gauss import GaussE,GaussJ
import parserr
from Jacobi_Seidel import IterativeSolver

###window functions
#setting the window
#the size of the window
#the tile of the window
window=tkinter.Tk()
window.geometry('800x600')
window.title("Solving system of linear equation")


###first label
#setting label
#packing label
#placing label
ls=tkinter.Label(window,text="Enter the equations:(max number of variablies 5)",font=('Arial Bold',20))
ls.pack()
ls.place(x=0,y=0)


###text area where the system of equation is going to enter
#setting textarea
#packing textarea
#placing textarea
txt=tkinter.Text(window,width=25,height=5,font=('Arial Bold',14))
txt.pack()
txt.place(x = 5,y = 45)

###presion label for rounding
#setting label
#packing label
#placing label
pre=tkinter.Label(window,text="precision",font=('Arial Bold',14))
pre.pack()
pre.place(x=5,y=160)

##text area where presion is going to enter
pres=tkinter.Entry(window,width=50)
pres.place(x =5 , y = 185,width=150,height=20)


###Dropbox for choosing the methode
#serting Dropbox
#placing Dropbox
#setting values
#setting initial value
v = tkinter.StringVar()
systems=ttk.Combobox(window,textvariable=v,font=('Arial Bold',14))
systems.place(x=300,y=50)
systems['values']=("1.Gauss Elimination","2.Gauss Jordan","3.LU Decomposition","4.Gauss Seidil","5.Jacobi Iteration")
systems.current(0)



###Dropbox for choosing the methode diagonlization
#serting Dropbox
#placing Dropbox
#setting values
#setting initial value
systems1=ttk.Combobox(window,font=('Arial Bold',14))
systems1.place(x=300,y=85)
systems1['values']=("1.Downlittle Form","2.Crout Form","3.Cholesky Form")
systems1.current(0)


###second label for intinals
#setting label
#packing label
#placing label
lsI=tkinter.Label(window,text="Initials:(defult=zeroes)",font=('Arial Bold',16))
lsI.pack()
lsI.place(x=300,y=140)


###text area where the innitals for iteration methode will be used
#setting textarea
#placing textarea
initials=tkinter.Entry(window,width=50)
initials.place(x = 300, y = 170,width=150,height=20)


###third label for iterations
#setting label
#packing label
#placing label
lsS1=tkinter.Label(window,text="number of iteration:(defuly=500)",font=('Arial Bold',15))
lsS1.pack()
lsS1.place(x=300,y=210)


###text area where the number of iteration for iteration methode will be used
#setting textarea
#placing textarea
txt1=tkinter.Entry(window,width=50)
txt1.place(x = 300, y = 240,width=150,height=20)

###fourth label for error
#setting label
#packing label
#placing label
lsS2=tkinter.Label(window,text="Error:(defult=10^-6)",font=('Arial Bold',15))
lsS2.pack()
lsS2.place(x=300,y=290)

###text area where the error for iteration methode will be used
#setting textarea
#placing textarea
txt2=tkinter.Entry(window,width=50)
txt2.place(x = 300,y = 320,width=150,height=20)


############### answer screenn #####################
###answer
ans=tkinter.Label(window,text="Answer",font=('Arial Bold',15))
ans.pack()
ans.place(x=5,y=290)

screen=tkinter.Label(window, bg="white",text=" ",anchor='nw',font=('Arial Bold',14))
screen.pack()
screen.place(x=5,y=320,width=250,height=280)

### time
tm=tkinter.Label(window,text="Time:",font=('Arial Bold',15))
tm.pack()
tm.place(x=350,y=380)

### converg
con=tkinter.Label(window,text="convergance:",font=('Arial Bold',15))
con.pack()
con.place(x=350,y=450)

###########Button and thier function ##################
#########function for main logic of button
def solver():
   ###defult values
   rou=5
   iterations=500
   errors=10**-6
   ans=[]
   es=txt.get("1.0","end-1c")
   es = es.replace(" ", "")
   obj=parserr.getLists()

   #roundoff
   if(len(pres.get().replace(" ", ""))!=0):
      rou=int(pres.get().replace(" ", ""))

   #iterations
   if(len(txt1.get().replace(" ", ""))!=0):
      iterations = int(txt1.get().replace(" ", ""))

   #errors
   if(len(txt2.get().replace(" ", ""))!=0):
      errors = float(txt2.get().replace(" ", ""))

   varss=obj.parsingVar(es+"\n")
   c=obj.validations(es+"\n") 
   if(c==False or isinstance(varss, str)):
      print(c)
      screen.config(text="error")
      tkinter.messagebox.showinfo( "error message","Error")
      return None
   noVar=len(varss)

   if(noVar>c ):
      screen.config(text="Infinte number of solutions")
      return None

   cofs,valuse=obj.parsingCoff(varss,es+"\n")
   tkinter.messagebox.showinfo( "order of variables",varss)
   k=int(systems.get()[0])

   if(k==4 or k==5):
      inital=[ 0 for i in range(noVar) ]

      if(len(initials.get().replace(" ", ""))!=0):
         temp=initials.get().replace(" ", "")
         queue=[]
         nex=0
         for p in temp:
            if(p==","):
              z="" 
              while(len(queue)>0):
                z=z+queue.pop(0)
              inital[nex]=float(z)
              nex+=1
            else:
              queue.append(p)
         z="" 
         while(len(queue)>0):
            z=z+queue.pop(0)
         inital[nex]=float(z)
          
      if(k == 4):
         iterativeSolver = IterativeSolver.iterSolver(cofs,valuse,iterations,inital,errors,rou,4)
         guess,crit,time = iterativeSolver.Solveit()
         print(guess,crit,time) 
      else:
         iterativeSolver = IterativeSolver.iterSolver(cofs,valuse,iterations,inital,errors,rou,5)
         guess,crit,time = iterativeSolver.Solveit()
         print(guess,crit,time)
   elif(k==1): 
     gas=GaussE.GaussE()
     ans=gas.solve(noVar,cofs,valuse,rou)
   elif(k==2):
     gas=GaussJ.GaussJ()
     ans=gas.solve(noVar,cofs,valuse,rou)
   else:

      return None     
   if(isinstance(ans, str)):
      screen.config(text=ans)
      tm.config(text="Time:")
      con.config(text="convergance:")
   else:
      tm.config(text="Time:"+str(ans[1])+"sec")
      con.config(text="convergance:"+str(ans[2]))
      answer="   "
   
      for k in range(noVar):
         answer=answer+""+str(varss[k])+" = "+str(ans[0][k])+"\n"

      screen.config(text=answer)   
      if(len(ans)==4):
         answer=answer+ans[3]
         screen.config(text=answer)  

B = tkinter.Button(window, text ="solve", command = solver)
B.pack()
B.place(x=5,y=210,width=210)

## main loop for the program
window.mainloop()

