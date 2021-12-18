class getLists:
  
  ## function to validate some inputs
  def validations(self,string):
    lenth=len(string)
    i=0
    spcI=[]
    eqI=[]
    operations=["+","-","."]
    print(lenth)
    while i < lenth:

      if  (string[i] == "\n"):
         spcI.append(i)
      elif(string[i] == "="):
        eqI.append(i)
      if(i>0 and ( string[i-1] in operations and string[i] in  operations)):
        return False
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

    i=i+1      
    return len(eqI)    
 
   
  ###function to get variables  
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
       elif(flage==True):
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
    print(var)     
    return var



  ### coeffficent matrix
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
           if(len(queue1) and i=="-" and queue1[0]=="-"):
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
    
    print(cofs)
    print(value)
    return cofs,value
