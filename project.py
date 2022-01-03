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
import fixedPoint
#####################
from matplotlib.figure import Figure
import numpy as np
from sympy import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg







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
lsS2=tkinter.Label(window,text="Error:(default=10^-6)",font=('Arial Bold',15))
lsS2.pack()
lsS2.place(x=300,y=290)

###text area where the error for iteration methode will be used
#setting textarea
#placing textarea
txt2=tkinter.Entry(window,width=50)
txt2.place(x = 300,y = 320,width=150,height=20)


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

###########Button and thier function ##################
#########function for main logic of button
def solver():
 try:
  
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
  if (checkFirst==1 or checkFirst==2 or checkFirst==3 or checkFirst==4 or checkFirst==5) and systems.get()[1]==".":
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

   ans=[]
   if(checkFirst==6):
      og=bracketingMethodSolver.bracketingMethodSolver()
      print(var)
      ans=og.bisect(intial,intial2,tol,var,rou,maxiter)
      if(not(isinstance(ans, str))):
         print("aaser")
         print(ans)
         
         x = Symbol('x')
         function = sympify(var)
         function = lambdify(x, function)
         Xaxis = np.linspace(intial-1,-intial2+1,10*10)
         if intial>intial2:
            Xaxis = np.linspace(intial2-1,-intial+1,10*10)

         list1=ans[0]
         list2=ans[1]
         for i in range(1,ans[2]+1):
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
 
    
   elif(checkFirst==7):
      ans=bracketingMethodSolver.regula(intial,intial2,tol,var,rou)
    
   elif(checkFirst==8):

      sol=fixedPoint.fixedPoint(tol,maxiter,intial,var,intial,intial2)
      ans=sol.solve()

   elif(checkFirst==9):

      
      sol=NewtonRaphson.NewtonRaphson(tol,maxiter,rou,intial,var)
      ans=sol.solve()

   else:
                  
      sol=Secant.Secant(0.00001,maxiter,rou,intial,intial2,var)
      ans=sol.solve()

  if(isinstance(ans, str)):
      if(len(ans)>27):
         screen.config(text=ans[0:24]+"\n"+ans[24:])
      else:
         screen.config(text=ans)  
      tm.config(text="Time:")
      con.config(text="convergance:")
 except:
      traceback.print_exc()
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


##########################
def make():
 def bisect(a,b,tol,f):
    xr = 0
    i = 0
    a_list = []
    b_list = []
    a_list.append(a)
    b_list.append(b)
    while(f(xr) != 0):
        xrnew = (a+b)/2.0
        i += 1
        print(f'lower limit : {a} | upper limit : {b} | root: {xrnew} | f(a) = {f(a)} | f(b) = {f(b)} | f(xr) = {f(xrnew)} | error = {abs(xrnew-xr)}')
        if(abs(xr-xrnew) < tol):
            xr = xrnew
            break
        value = f(a)*f(xrnew)
        xr = xrnew
        if(value < 0):
            b = xrnew
        elif(value > 0):
            a=xrnew
        else:
            break
        a_list.append(a)
        b_list.append(b)
    print(f'xr = {xr} and no. of iterations = {i}')
    return a_list,b_list,i


 x = Symbol('x')

 function = sympify("x^4-2*x^3-4*x^2+4*x+4")

 function = lambdify(x, function)
 list1,list2,n= bisect(-2,-1,10**-1,function)
 Xaxis = np.linspace(-2,-1,10*10)
 
 


 for i in range(1,n+1):
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
 


chx = tkinter.Button(window, text ="Show graph", command = make)
chx.pack()
chx.place(x=550,y=570,width=150)

############################





## main loop for the program
window.mainloop()

