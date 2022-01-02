import math
from sympy import *
from sympy.abc import a, b, c, x
class fixedPoint:
    def __init__(self,errorStop,iterMax,initialX,f):
        self.errorStop = errorStop
        self.iterMax = iterMax
        self.f = f
        self.initialX = initialX


    def Get_G(f):
        X = Symbol('x')
        solve_undetermined_coeffs(f,[x],x)        
        return 

    def solve(self):
        Xi = self.initialX
        preXi = self.initialX
        crit = ""
        i = 1
        G = self.__Get_G()
        print(G)
#        while i <= self.iterMax:
 #           preXi = Xi
  #          Xi = G(Xi)
   #         error = math.abs((Xi-preXi)/Xi)
#
#            if error < self.errorStop:
 #               crit = "Converged"
  #              return [Xi,i,crit,G]
#
 #       crit = "Diverged"
  #      return [Xi,i,crit,G]

def Get_G():
        return  

x = Symbol('x')
y = Symbol('y')
X = Symbol('X')
f = sympify("x**a+b*x+1")
print(f)
print(solve_linear(lhs = x**2+X*b+1,exclude=[b,X]))        
