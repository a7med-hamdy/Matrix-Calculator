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
        gets the appropriate G(x) by comparing the interval got from solving
        |G`(x)| < 1 and checking whether the initial X belongs in this interval
        for convergance

        returns: appropriate G(x)

    """
    def Get_G(self):
        #x = Symbol("x",real=True,postive =True)
        y = Symbol("y",real = True,positive = True) #symbol to replace it with
        X = Symbol("X",real = True,positive = True) #orignial symbol
        farray = [] #all iterations of F(x) 
        Garray = [] #all possible G(x)
        G_primeArray = [] # all possible G`(x)
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
        print(farray)
        # solve in x in terms of y in each of the iterations stored in farray
        # and store them in Garray and their derivatives in G_primeArray 
        for i in range(len(farray)):
            g = solve(farray[i],symbols=[X],exclude=[y],domain= S.Reals)
            for j in range(len(g)):
                if "I" not in str(g[j]):
                    g_prime = diff(g[j],y)
                    Garray.append(g[j])
                    G_primeArray.append(g_prime)

        print(Garray)
        print(G_primeArray)
        #get the appropriate G(x) and return it
        for i in range(len(G_primeArray)):
            try:
                if(solve(abs(G_primeArray[i]) < 1).as_set().contains(self.initialX)):
                    return Garray[i]
                #if(not solve(abs(G_primeArray[i]) < 1).as_set().is_disjoint(Interval(self.intervala,self.intervalb))):
                 #   return Garray[i]
            except:
                print(G_primeArray[i])
                return Garray[i]


    """
        solving function that gets G(x) then iterates using the fixed point
        algorithm and return the result & criteria of convergence

        returns:
        G: G(x)
        Xi: last iteration of X
        time : runtime of the code
        crit : criteria of convergence "Converged" | "Diverged"
        i : number of iterations
    """
    def Solve(self):
        Xi = self.initialX
        preXi = self.initialX
        crit = ""
        i = 1
        begin_time = timer()
        G = self.Get_G()
        print("G(X) =", G)
        print("Xi = ",Xi)
        #get the function G(x)
        Gx = lambdify(self.X,G)
        print(Gx(Xi))
        #begin loop
        while i <= self.iterMax:
            #store previous Xi
            preXi = copy.deepcopy(Xi)
            #substitute in G(x)
            Xi = copy.deepcopy(sigfig.round(Gx(Xi), sigfigs = self.significantFigs))
            print("iteration no:"+str(i),Xi)
            #calculate the error
            error = abs((Xi-preXi)/Xi)

            #check if the error < Es to break and return results
            if error < self.errorStop:
                crit = "Converged"
                time = timer()- begin_time 
                print("Runtime : "+str(time)+" seconds")
                return [Xi,i,crit,G,time]
            i+= 1
        #if the loop is done then the value diverged
        #return the results
        crit = "Diverged"
        time = timer() - begin_time
        print("Runtime = "+str(time)+" seconds")
        return [Xi,i,crit,G,time]

#x = Symbol('x',real = True,positive = True)
#f = x**2 - 2*x -3

#fixed = fixedPoint(10**-2,100,0,f,5)

#fixed.Solve()
