### this is the imports
import tkinter
from tkinter.constants import X
import tkinter.messagebox
from tkinter import ttk
import numpy as np
from Gauss import GaussE,GaussJ
import parserr
from Jacobi_Seidel import IterativeSolver
import LU_decomposer

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
ls=tkinter.Label(window,text="Enter the equations:(max number of variables is 5)",font=('Arial Bold',20))
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
systems=ttk.Combobox(window,textvariable=v,font=('Arial Bold',14), state = "readonly")
systems.place(x=300,y=50)
systems['values']=("1.Gauss Elimination","2.Gauss Jordan","3.LU Decomposition","4.Gauss Seidel","5.Jacobi Iteration")
systems.current(0)



###Dropbox for choosing the methode diagonlization
#serting Dropbox
#placing Dropbox
#setting values
#setting initial value
systems1=ttk.Combobox(window,font=('Arial Bold',14), state = "readonly")
systems1.place(x=300,y=85)
systems1['values']=("1.Doolittle Form","2.Crout Form","3.Cholesky Form")
systems1.current(0)


###second label for intinals
#setting label
#packing label
#placing label
lsI=tkinter.Label(window,text="Initials:(default=zeroes)",font=('Arial Bold',16))
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
lsS1=tkinter.Label(window,text="number of iteration:(default=500)",font=('Arial Bold',15))
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
lsS2=tkinter.Label(window,text="Error:(default=10^-6)",font=('Arial Bold',15))
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
screen.place(x=5,y=320,width=290,height=280)

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
  try: 
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

   #checkword
   while es[0]=="\n" :
     es=es[1:]

   while es[-1]=="\n" :
     es=es[0:-1]

   # varaible
   varss=obj.parsingVar(es+"\n")
   # validity
   c=obj.validations(es+"\n") 
   # check that equation and varaiables is right
   if(c==False or isinstance(varss, str)):
 
      screen.config(text="error in systems")
      tkinter.messagebox.showinfo( "error message","Error enter\nright system")
      return None
   # check that equation equal numbre of varaibles
   noVar=len(varss)
   # check that equation and varaiables are equal
   if(noVar!=c ):
      screen.config(text="not square matrix")
      return None
   # check that varablies is less than 5
   if(noVar>5 ):
      screen.config(text="more than 5 variables")
      return None
   # A (coefficient)  and B (value)
   cofs,valuse=obj.parsingCoff(varss,es+"\n")
   tkinter.messagebox.showinfo( "order of variables",varss)

   # the number of choosen system
   k=int(systems.get()[0])

   # the choosen system
   #gauss seidal and jacobi iteration
   if(k==4 or k==5):
      #intinal values
      inital=[ 0 for i in range(noVar) ] #inital for iteraitve method
      ini=initials.get().replace(" ", "")

      #iterations
      if(len(txt1.get().replace(" ", ""))!=0):
         iterations = int(txt1.get().replace(" ", ""))

   #errors
      err=txt2.get().replace(" ", "")
      if(len(err)!=0):
         if("^" in err):
            num=""
            power=""
            found=False
            for i in err:
               if(i=="^"):
                  found=True
               elif(found):
                  power=power+i
               else:
                  num=num+i
            errors=float(num)**float(power)         
         else:   
            errors = float(err)
            
      #check if the user enter inintals and enter it right
      if(len(ini)!=0):
         temp=ini
         queue=[]
         nex=0
         fasla=0
         for p in temp:
            if(p==","):
              z=""
              fasla+=1 
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
         if(noVar-1!=fasla):
            tkinter.messagebox.showinfo( "enter the right number of variable","intials not\n equal variable")
            return None
      #Gauss seidal  #Jacobi iteration
      iterativeSolver = IterativeSolver.iterSolver(cofs,valuse,iterations,inital,errors,rou,k)
      ans = iterativeSolver.Solveit()
    
   elif(k==1): 
     gas=GaussE.GaussE()
     ans=gas.solve(noVar,cofs,valuse,rou)
   #gauss Jordan
   elif(k==2):
     gas=GaussJ.GaussJ()
     ans=gas.solve(noVar,cofs,valuse,rou)
   #LU Decompossection
   else:
     LU=LU_decomposer.LU_decomposer(np.array(cofs,float),rou,valuse) 
     #way of decomostions
     wy=int(systems1.get()[0])
     ans=LU.decompose(wy)
   #print error mesg if error happen    
   if(isinstance(ans, str)):
      if(len(ans)>27):
         screen.config(text=ans[0:24]+"\n"+ans[24:])
      else:
         screen.config(text=ans)  
      tm.config(text="Time:")
      con.config(text="convergance:")
   #print answer from answer array   
   else:
      tm.config(text="Time:"+str( round(ans[1],8) )+" sec")
      con.config(text="convergance:"+str(int(ans[2])))
      answer="   "
   
      for k in range(noVar):
         answer=answer+""+str(varss[k])+" = "+str(ans[0][k])+"\n"

      screen.config(text=answer)   
      if(len(ans)==4):
         answer=answer+ans[3]
         screen.config(text=answer) 
  except:  
      tkinter.messagebox.showinfo( "some Error","error in input")
      screen.config(text="error in input") 

B = tkinter.Button(window, text ="solve", command = solver)
B.pack()
B.place(x=5,y=210,width=210)
###################### check button ###################
### this button is for check the order of variable to enter the inintails 
def getVars():
   es=txt.get("1.0","end-1c")
   es = es.replace(" ", "")
   obj=parserr.getLists()
   varss=obj.parsingVar(es+"\n")
   c=obj.validations(es+"\n") 
   if(c==False or isinstance(varss, str)):
      print(c)
      tkinter.messagebox.showinfo( "error message","Error")
   else:   
      tkinter.messagebox.showinfo( "vars order",varss)



check = tkinter.Button(window, text ="Show variables order", command = getVars)
check.pack()
check.place(x=630,y=210,width=150)

## main loop for the program
window.mainloop()

