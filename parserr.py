class getLists:
   

  
  def parsing(self,string):
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
          if(len(queue)):  
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
          print(i,"here2")
          return "not a right sign"
    print(var)     
    return var   
 
    
