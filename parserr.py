class pars:
  
  ## function to validate some inputs
  # @ parameter string : the systems of equatians  
  # returns numebr of systems

  def validations(self,string):
    lenth=len(string)
    i=0
    spcI=[]
    eqI=[]
    operations=["+","-","."]

    while i < lenth:

      if  (string[i] == "\n"):
         spcI.append(i)
      elif(string[i] == "="):
        eqI.append(i)
      if(i>0 and ( string[i-1] in operations and string[i] in  operations)):
        return False
      i=i+1   
    if(len(spcI)!=len(eqI)):
      return False
    else:
      for i in range(len(eqI)):
        if(eqI[i]>spcI[i]):
          return False
        if(i==0):
          if(eqI[i]==0 or spcI[i]-eqI[i]==1):
            return False
        else:
           if(eqI[i]-spcI[i-1]<=1 or spcI[i]-eqI[i]==1):
            return False
   
          
    return len(eqI)    
 
   
  ###function to get variables
  # # @ parameter string : the systems of equatians  
  # returns array of variable 
  def parsingVar(self,string):
    queue = []
    var=[]
    operations=["+","-","=","\n"]
    flage=False
    for z in range(len(string)):
       i=string[z]
       if(i.isalpha()):
          queue.append(i)
          flage=True
       
       elif((i in operations) and flage):
          flage=False
          if(len(queue)>0 and len(queue)<3):  
             x=""
             while(len(queue)>0):
                x=x+queue.pop(0)
             if(x not in var):   
                var.append(x)   
          else:
             return "Wrong formate"
       elif(flage==True and i.isnumeric()):
          queue.append(i)
       elif(i in operations):
          if(i=="-" and (z==0 or string[z-1]=="=" or string[z-1]=="\n")):
             pass
          elif(not(string[z-1].isnumeric())):
             return "Wrong formate"
       elif(i=="." ):
          if(z==0 or (not(string[z-1].isnumeric())) and not(string[z+1].isnumeric())):
              return "Error . entered wrong"
       elif(not(i.isnumeric())):
       
          return "not a right sign"
       if(len(queue)>2):
         return "weird variable"
    return var



  ### coeffficent matrix
  # @ parameter string : the systems of equatians  
  # @ PARAMTER  VARABLIES ARRAY
  # returns 2darray of coffiecent and 1d values array
  
  def parsingCoff(self,var,string):
    queue1 = []
    queue2 = []
    n=len(var)

    cofs=[ [ 0 for i in range(n) ] for j in range(n) ]
    value=[ 0 for i in range(n) ]
    row=0
    bf=0
    operations=["+","-","=","\n"]
    flage=False
    for z in range(len(string)):
      
       i=string[z]
       
       if((i.isnumeric() or i=="-" or i==".") and not(flage)):
           if(len(queue1)>0 and i=="-"):
        
             y=""
             if(len(queue1)):
              while(len(queue1)>0):
                y=y+queue1.pop(0)
             if(bf==0):     
              value[row]=value[row]-float(y)  
             else:
              value[row]=value[row]+float(y)           
             queue1.append(i)
           else:
             queue1.append(i)
           
       elif(i.isalpha()):
           queue2.append(i)
           flage=True
           
       elif((i in operations) and flage):
           flage=False
           x=""
           y=""
           l=0
           if(len(queue2)):  
             while(len(queue2)>0):
                x=x+queue2.pop(0)
           if(len(queue1)):
             while(len(queue1)>0):
                y=y+queue1.pop(0)
           else:
             y="1"
          ###finding index of the varablies
           if(i=="-"):
             queue1.append(i)
           for k in range(n):
             if(var[k]==x):
               l=k
               break
           if(y=="-"):
             y="-1"
           if(bf==0):     
             cofs[row][l]=cofs[row][l]+float(y)  
           else:
             cofs[row][l]=cofs[row][l]-float(y)
             
       elif((i in operations) and not(flage)):
           y=""
           if(len(queue1)):
             while(len(queue1)>0):
                y=y+queue1.pop(0)
           if(bf==0):     
             value[row]=value[row]-float(y)  
           else:
             value[row]=value[row]+float(y) 
       elif(flage==True):
           queue2.append(i)
           
       if(i=="\n"):
           row=row+1
           bf=0
       if(i=="="):
           bf=1
       
          


    return cofs,value






  ###helping funtion for parsing
  # @ parameter string : the non linaer equation equatians in array
  #@ parameter i : the index wants to br checks
  # returns true of false
  def _checkB(self,string,i):
    fs=i-1
    sc=i+1
    print(string[i])
    operations=["+","-","."]
    while string[fs]!=")" and  string[fs]!="=":
      print("das",string[fs],fs)
      if string[fs]=="(" or  string[fs]=="^":
        return False
      else:
        fs-=1

    while sc<len(string) and (string[sc]!="E" and string[sc]!="s" and string[sc]!="E") :
      print("sas",string[sc],sc)
      if string[sc]==")":
        return False
      else:
        sc+=1
     
    return True



  ### funtion for parsing non linear
  # @ parameter string : the non linaer equation equatians  
  # returns string of equation to be simpfiy
  
  def parsingNonlinear(self,string):
    last=[]

   #parsing the sign for simpfiy
    for i in range(len(string)):
   
      if string[i]=="e":
        last.append("E")
      elif string[i]=="p":
        last.append("^")
      elif string[i]=="x" and i>0 and  string[i-1]=="e":
        pass
      else:
        last.append(string[i])


    #dealing with the eqaution before and after the equal sign  
    found=False   
    x=0
    z=-1
    i=0
    while i <len(last):
    
      if last[i]=="=" and last[-1]!="=":
        x=i
        found=True
      if last[i]=="0":
        z=i
      if found:

        if (last[i]=="c" or last[i]=="s" or last[i]=="E") and  not(last[i-1].isnumeric()):
  
          if last[i-1]=="+":
            last[i-1]="-"
          elif last[i-1]=="=":
            last.insert(i,"-")
            i+=1

          elif last[i-1]=="-":
            last[i-1]="+"
          
        elif ((last[i].isnumeric() and  not(last[i-1].isnumeric())) or  (last[i]=="x"and  not(last[i-1].isnumeric()))) and self._checkB(last,i) :
          print(last[i],i)
          if last[i-1]=="+":
            last[i-1]="-"
          elif last[i-1]=="=":
            last.insert(i,"-")
            i+=1
          elif last[i-1]=="-":
            last[i-1]="+"
     
      i+=1



    if found:
      last.pop(x)
         
      x= "".join(last)

      return x.replace(" ", "")
    else:
      return False  
    
