### this is the imports
import traceback
from tkinter import*
import tkinter 
from tkinter.constants import X
import tkinter.messagebox
from tkinter import Canvas, ttk
import numpy as np
from sympy.series.formal import simpleDE
from Gauss import GaussE,GaussJ
import parserr
from Jacobi_Seidel import IterativeSolver
import LU_decomposer
###########################################
import bracketingMethodSolver
import NewtonRaphson
import Secant
from Fixed_Point import fixedPoint
#####################
from sympy import *
from sympy.parsing.sympy_parser import implicit_multiplication_application, standard_transformations,convert_xor
from matplotlib.figure import Figure
import numpy as np
from sympy import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


transformations = (standard_transformations +(implicit_multiplication_application,convert_xor))



###window functions
#setting the window
#the size of the window
#the tile of the window
window=tkinter.Tk()
window.geometry('1400x600')
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
systems['values']=("1.Gauss Elimination","2.Gauss Jordan","3.LU Decomposition","4.Gauss Seidel","5.Jacobi Iteration",
                     "6.Bisection","7.False-Position","8.Fixed point","9.Newton-Raphson","10.Secant Method.")
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
lsS1=tkinter.Label(window,text="number of iteration:(default=500)\n(50 for nonlinear)",font=('Arial Bold',15))
lsS1.pack()
lsS1.place(x=300,y=200)


###text area where the number of iteration for iteration methode will be used
#setting textarea
#placing textarea
txt1=tkinter.Entry(window,width=50)
txt1.place(x = 300, y = 260,width=150,height=20)

###fourth label for error
#setting label
#packing label
#placing label
lsS2=tkinter.Label(window,text="Error:(default=10^-6)\n(10^-5 for nonlinear)",font=('Arial Bold',14))
lsS2.pack()
lsS2.place(x=300,y=290)

###text area where the error for iteration methode will be used
#setting textarea
#placing textarea
txt2=tkinter.Entry(window,width=50)
txt2.place(x = 300,y = 350,width=150,height=20)


############## for non linear ######################

###fifth label for first interval
#setting label
#packing label
#placing label
inilabl1=tkinter.Label(window,text="Interval a/first initial",font=('Arial Bold',14))
inilabl1.pack()
inilabl1.place(x=550,y=30)

###text area for first interavl
#setting textarea
#placing textarea
ini1=tkinter.Entry(window,width=50)
ini1.place(x = 550,y = 55,width=100,height=20)

###sixth label for second interval
#setting label
#packing label
#placing label
inilabl2=tkinter.Label(window,text="Interval b/second initial",font=('Arial Bold',14))
inilabl2.pack()
inilabl2.place(x=550,y=75)

###text area for second interavl
#setting textarea
#placing textarea
ini2=tkinter.Entry(window,width=50)
ini2.place(x = 550,y = 100,width=100,height=20)

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
############## the graph frame #######################
frame = Frame(window)
frame.config(bg="white")
frame.pack(expand=True, fill=BOTH)
frame.place(x=785,y=10,width=610,height=585)
############control variavles################
zzz=[]
pos=0            
###########polting function ###########################

 ### funtion for plot the steps of Brackting function
  # @ parameter list1 : a steps array of side of Brackting
  # @ parameter list2 : a steps array of side of Brackting
  # @ parameter itr : number of iteraction
  # @ parameter intial : the first iniital user entered 
  # @ parameter intial2 :the second iniital user entered 
  # @ parameter var : the function 

def plotbisection(list1,list2,itr,intial,intial2,var):
   global zzz
   global pos
   zzz=[]
   pos=0
   for widget in frame.winfo_children():
    widget.destroy()
   x = Symbol('x')
   function = lambdify(x, var)
   Xaxis = np.linspace(intial-1,intial2+1,10*10)
   if intial>intial2:
      Xaxis = np.linspace(intial2-1,intial+1,10*10)
   for i in range(1,itr+1):
      f=Figure(figsize=(20,20),dpi=100)
      a =f.add_subplot(1,1,1)
      a.plot(Xaxis, function(Xaxis),'r')
      a.axhline(color="black", linewidth=2)
      a.axvline(color="black", linewidth=2)
      a.grid()
      a.axvline(x=list1[i-1])
      a.axvline(x=list2[i-1])
      a.ticklabel_format(useOffset= False, style='plain')
      zzz.append(f)
   canvas=FigureCanvasTkAgg(zzz[pos],master=frame)
   canvas.get_tk_widget().pack(side=LEFT,expand=False,fill=None)

##################################################################
 ### funtion for plot the fixed piont functions
  # @ parameter intial : the ff(x) functions
  # @ parameter driv : the g(x) function
def plotnormal(intial,driv):
   global zzz
   global pos
   zzz=[]
   pos=0
   for widget in frame.winfo_children():
    widget.destroy()
   x = Symbol('x')
   y = Symbol('y',real = True,positive = True)
   function2 = lambdify(y,driv)

   Xaxis = np.linspace(intial-20,intial+20,10*10)
   ylist=[]
   for i in Xaxis:
      ylist.append(function2(i))
   yaxis = np.array(ylist)
   f=Figure(figsize=(20,20),dpi=100)
   a =f.add_subplot(1,1,1)
   a.axhline(color="black", linewidth=2)
   a.axvline(color="black", linewidth=2)
   a.grid()
   a.plot(Xaxis, Xaxis,'g')
   a.plot(Xaxis, yaxis,'b')
   canvas=FigureCanvasTkAgg(f,master=frame)
   canvas.get_tk_widget().pack(side=LEFT,expand=False,fill=None)

#####################################################################
 ### funtion for plot the drivative of the function
  # @ parameter intial : the first iniital user entered 
  # @ parameter intial2 :the second iniital user entered 
  # @ parameter driv : the drivatev function  

def plotmaker(intial,intial2,driv):
   global zzz
   global pos
   zzz=[]
   pos=0
   for widget in frame.winfo_children():
    widget.destroy()
   x = Symbol('x')
   function2 = lambdify(x,driv)

   Xaxis = np.linspace(intial-10,intial2+10,10*10)
   if intial>intial2:
      Xaxis = np.linspace(intial2-10,intial+10,10*10)
   ylist=[]
   for i in Xaxis:
      ylist.append(function2(i))
   yaxis = np.array(ylist)
   f=Figure(figsize=(20,20),dpi=100)
   a =f.add_subplot(1,1,1)
   a.axhline(color="black", linewidth=2)
   a.axvline(color="black", linewidth=2)
   a.grid()
   a.plot(Xaxis, yaxis,'b')
   canvas=FigureCanvasTkAgg(f,master=frame)
   canvas.get_tk_widget().pack(side=LEFT,expand=False,fill=None)
###########Button and thier function ##################
#########function for main logic of button
def solver():
 try:
  global zzz
  global pos
  #reading input
  es=txt.get("1.0","end-1c")
  es = es.replace(" ", "")
  obj=parserr.pars()

   #checkword
  while es[0]=="\n" :
     es=es[1:]

  while es[-1]=="\n" :
     es=es[0:-1]
     
   #check HOWTO SOLVE LINAEAR  OR NON-LINEAR
  checkFirst=int(systems.get()[0])  
  #linrat systenm
  if (checkFirst==1 or checkFirst==2 or checkFirst==3 or checkFirst==4 or checkFirst==5) and systems.get()[1]==".":
   ## remove all the graphs
   zzz=[]
   pos=0
   for widget in frame.winfo_children():
    widget.destroy()  
   ###defult values
   rou=5
   iterations=500
   errors=10**-6
   ans=[]

   #roundoff
   if(len(pres.get().replace(" ", ""))!=0):
     rou=int(pres.get().replace(" ", ""))
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

  ### the new code part  of thenin linear equation      
  else:
   #defults
   rou=None

   maxiter=50

   intial=None

   intial2=None

   tol=10**-5

   if(len(pres.get().replace(" ", ""))!=0):
     rou=int(pres.get().replace(" ", ""))
   
   var=obj.parsingNonlinear(es)

   #taking error
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
            tol=float(num)**float(power)         
         else:   
            tol = float(err)

   #iterations
   if(len(txt1.get().replace(" ", ""))!=0):
         maxiter = int(txt1.get().replace(" ", ""))
   
   #inital1
   if(len(ini1.get().replace(" ", ""))!=0):
         intial = float(ini1.get().replace(" ", ""))


   #inital2
   if(len(ini2.get().replace(" ", ""))!=0):
         intial2 = float(ini2.get().replace(" ", ""))


   var = parse_expr(var,transformations=transformations)


   ans=[]
   # check if the initial is entered and make the bisection
   if(checkFirst==6) and intial!=None and  intial2!=None:
      og=bracketingMethodSolver.bracketingMethodSolver()
      ans=og.bisect(intial,intial2,tol,var,rou,maxiter)
      if(not(isinstance(ans, str))):
         plotbisection(ans[0],ans[1],ans[2],intial,intial2,var)
         screen.config(text=ans[3])
         tm.config(text="Time:"+str( round(ans[5],8) )+" sec")
         con.config(text="convergance:"+str(ans[2])) 
        
   # check if the initial is entered and make the false postion 
   elif(checkFirst==7) and intial!=None and  intial2!=None:
      og=bracketingMethodSolver.bracketingMethodSolver()
      ans=og.regula(intial,intial2,tol,var,rou,maxiter)
      if(not(isinstance(ans, str))):
         plotbisection(ans[0],ans[1],ans[2],intial,intial2,var)
         screen.config(text=ans[3])
         tm.config(text="Time:"+str( round(ans[5],8) )+" sec")
         con.config(text="convergance:"+str(ans[2]))
         
   # check if the initial is entered and make the fixed point function 
   elif(checkFirst==8)  and intial!=None:
      og=fixedPoint.fixedPoint(tol,maxiter,intial,var,rou)
      ans=og.Solve()
      if(not(isinstance(ans, str))):
         plotnormal(intial,ans[3])
         screen.config(text="x = "+str(ans[0])+"\n"+ans[2] )
         tm.config(text="Time:"+str( round(ans[4],8) )+" sec")
         con.config(text="convergance:"+str( ans[1] ))

   # check if the initial is entered and make the nrwton rasphorad
   elif(checkFirst==9)  and intial!=None:
      og=NewtonRaphson.NewtonRaphson(tol,maxiter,rou,intial,var)
      ans=og.solve()
      plotmaker(intial,intial,ans[4])
      screen.config(text="x = "+str(ans[0])+"\n"+ans[2] )
      tm.config(text="Time:"+str( round(ans[3],8) )+" sec")
      con.config(text="convergance:"+str( ans[1] ))


   else:
      # check if the initial is entered and make the secant
      if  intial!=None and intial2!=None:            
         og=Secant.Secant(tol,maxiter,rou,intial,intial2,var)
         ans=og.solve()
         plotmaker(intial,intial,ans[4])
         screen.config(text="x = "+str(ans[0])+"\n"+ans[2] )
         tm.config(text="Time:"+str( round(ans[3],8) )+" sec")
         con.config(text="convergance:"+str( ans[1] ))
      # check mae this message if the initials is not entred in any of this one
      else:
         ans="enter initals"


  if(isinstance(ans, str)):
      if(len(ans)>27):
         screen.config(text=ans[0:24]+"\n"+ans[24:])
      else:
         screen.config(text=ans)  
      tm.config(text="Time:")
      con.config(text="convergance:") 
      zzz=[]
      pos=0
      for widget in frame.winfo_children():
         widget.destroy()
 except:
      traceback.print_exc()
      tkinter.messagebox.showinfo( "some Error","error in input")
      screen.config(text="error in input") 
      zzz=[]
      pos=0

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
check.place(x=540,y=145,width=150)

###########left and right incase of bisection################

#########left###############
def left():
 global pos
 if pos>0:
  for widget in frame.winfo_children():
    widget.destroy()  
  pos-=1 
  canvas=FigureCanvasTkAgg(zzz[pos],master=frame)
  canvas.get_tk_widget().pack(side=LEFT,expand=False,fill=None)
 

left = tkinter.Button(window, text ="<", command = left)
left.pack()
left.place(x=530,y=530,width=35)

#########right#############
def right():
 global zzz
 global pos 
 if pos<len(zzz)-1:  
  for widget in frame.winfo_children():
    widget.destroy()
  pos+=1
  canvas=FigureCanvasTkAgg(zzz[pos],master=frame)
  canvas.get_tk_widget().pack(side=LEFT,expand=False,fill=None)
 

right = tkinter.Button(window, text =">", command = right)
right.pack()
right.place(x=580,y=530,width=35)

############################





## main loop for the program
window.mainloop()

