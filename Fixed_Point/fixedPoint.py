import math
from sympy import *
from sympy.abc import x
from timeit import default_timer as timer
import sigfig
import copy
class fixedPoint:
    """
        Constructor 
        
        params:

        errorStop : stopping criteria

        iterMax : maximum number of iterations

        initialX : initial X

        f : function to iterate on

        significantFigs : significant figures 

    """
    def __init__(self, errorStop, iterMax, initialX, f,significantFigs): #intervala, intervalb, 
                    
        self.errorStop = errorStop
        self.iterMax = iterMax
        self.f = f
        self.initialX = initialX
        self.X = Symbol("y",real = True,positive = True)
        #self.intervala = intervala
        #self.intervalb = intervalb
        self.significantFigs = significantFigs


    """
        gets the all the iterations of G(x)

        returns: 
        Garray: array of all possible iterations of G(x)

    """
    def Get_G(self):
        #x = Symbol("x",real=True,postive =True)
        y = Symbol("y",real = True,positive = True) #symbol to replace it with
        X = Symbol("X",real = True,positive = True) #orignial symbol
        farray = [] #all iterations of F(x) 
        Garray = [] #all possible G(x)
        for i in range(len(self.f.args)):
            for j in range(len(self.f.args)):
                    expres = self.f.args[j].replace(x,X)
                    self.f = self.f.subs(self.f.args[j],expres)
        # get all possible solvings of F(x) by changing each symbol x with y in each
        # term except one term and storing these iterations in farray
        for i in range(len(self.f.args)):
            func = self.f
            for j in range(len(self.f.args)):
                if(i != j):
                    expres = func.args[j].replace(X,y)
                    func = func.subs(func.args[j],expres)
            farray.append(func)
        # solve in x in terms of y in each of the iterations stored in farray
        # and store them in Garray and their derivatives in G_primeArray 
        for i in range(len(farray)):
            g = solve(farray[i],symbols=[X],exclude=[y],domain= S.Reals)
            for j in range(len(g)):
                if "I" not in str(g[j]):
                    Garray.append(g[j])
        return Garray

    """
        solving function that iterates on all possible G(x)s using the fixed point
        algorithm and returns the one that converged, the result & criteria of convergence

        returns:
        G: G(x) that converged | if none converged then returns the last one used
        Xi: last iteration of X
        time : runtime of the code
        crit : criteria of convergence "Converged" | "all G(x)s found Diverged"
        i : number of iterations
    """
    def Solve(self):
        Xi = self.initialX
        preXi = self.initialX
        crit = ""
        i = 0
        c = 0
        begin_time = timer()
        G = self.Get_G()
        print("G(X) =", G)
        print("Xi = ",Xi)
        #get the function G(x)
        #print(Gx(Xi))
        if len(G) == 0:
            return "No G(x)s found"
        for j in range(len(G)):
            Xi = self.initialX
            preXi = self.initialX
            y = Symbol("y",real = True,positive = True) #symbol to replace it with
            Ga = G[j]
            Gx = (lambdify(y,G[j]))
            print(Gx(Xi))
            i = 0
            c = j
        #begin loop
            try:
                while i < self.iterMax:
                    #store previous Xi
                    preXi = copy.deepcopy(Xi)
                    #substitute in G(x)
                    Xi = copy.deepcopy(sigfig.round(Gx(Xi), sigfigs = self.significantFigs))
                    print("iteration no:"+str(i+1),Xi)
                    #calculate the error
                    error = abs((Xi-preXi)/Xi)

                    #check if the error < Es to break and return results
                    if error < self.errorStop:
                        crit = "Converged"
                        time = timer()- begin_time 
                        print("Runtime : "+str(time)+" seconds")
                        return [Xi,i+1,crit,G[j],time]
                    i+= 1
            except:
                if j != len(G)-1:
                    continue
                else:
                    #if the loop is done then the value diverged
                    #return the results
                    crit = "All G(x)s found Diverged"
                    time = timer() - begin_time
                    print("Runtime = "+str(time)+" seconds")
                    return [Xi,i+1,crit,G[j],time]
        #if the loop is done then the value diverged
        #return the results
        #crit = "All G(x)s found Diverged"
        #time = timer() - begin_time
        #print("Runtime = "+str(time)+" seconds")
        #return [Xi,i+1,crit,G[c],time]

      

#x = Symbol('x',real = True,positive = True)
#f = cos(x**2)-x+1

#fixed = fixedPoint(10**-8,50,1,f,5)

#fixed.Solve()
