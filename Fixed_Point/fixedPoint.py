import math
from sympy import *
from timeit import default_timer as timer
import sigfig
import copy
class fixedPoint:
    def __init__(self, errorStop, iterMax, initialX, f, intervala, intervalb,significantFigs):
        self.errorStop = errorStop
        self.iterMax = iterMax
        self.f = f
        self.initialX = initialX
        self.X = Symbol('y')
        self.intervala = intervala
        self.intervalb = intervalb
        self.significantFigs = significantFigs



    def Get_G(self):
        y = Symbol('y',real = True,positive = True)
        X = Symbol('X')
        x = Symbol('x',real = True,positive = True)
        #funcDiff = diff(func,x)
        farray = []
        Garray = []
        G_primeArray = []
        for i in range(len(self.f.args)):
            func = self.f
            for j in range(len(self.f.args)):
                if(i != j):
                    expres = func.args[j].replace(x,y)
                    func = func.subs(func.args[j],expres)
            farray.append(func)
        print(farray)
        for i in range(len(farray)):
            g = solve(farray[i],symbols=[x],exclude=[y],domain= S.Reals)
            for j in range(len(g)):
                if "I" not in str(g[j]):
                    g_prime = diff(g[j],y)
                    Garray.append(g[j])
                    G_primeArray.append(g_prime)

        print(Garray)
        print(G_primeArray)
        for i in range(len(G_primeArray)):
            try:
                if(not solve(abs(G_primeArray[i]) < 1).as_set().is_disjoint(Interval(self.intervala,self.intervalb))):
                    return Garray[i]
            except:
                
                print(G_primeArray[i])
                return Garray[i]


    def Solve(self):
        Xi = self.initialX
        preXi = self.initialX
        crit = ""
        i = 1
        G = self.Get_G()
        
        print("G(X) =", G)
        print("Xi = ",Xi)
        Gx = lambdify(self.X,G)
        print(Gx(Xi))
        while i <= self.iterMax:
            preXi = copy.deepcopy(sigfig.round(Xi, sigfigs = self.significantFigs))
            Xi = copy.deepcopy(sigfig.round(Gx(Xi), sigfigs = self.significantFigs))
            print(Xi)
            error = abs((Xi-preXi)/Xi)

            if error < self.errorStop:
                crit = "Converged"
                return [Xi,i,crit,G]

        crit = "Diverged"
        return [Xi,i,crit,G]

x = Symbol('x',real = True,positive = True)
f = x**3-x**2 - 2*x -3
#print(f)
fixed = fixedPoint(10**-8,100,0,f,1,4,5)

fixed.Solve()
