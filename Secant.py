from sympy import *
from sigfig import round
from timeit import default_timer as timer

class Secant:

    """
    constructor
    """
    def __init__(self, eps, max_iterations, precision, init_1, init_2, fun):
        self.eps = eps
        self.max_iterations = max_iterations
        self.precision = precision
        self.init_1 = init_1
        self.init_2 = init_2
        self.x = Symbol('x')
        self.fun = lambdify(self.x, fun)

    """
    solve function 
    """
    def solve(self):
        begin_time = timer() #measure the execution time
        criteria = ""
        Ea = 100
        iterations = 0
        X1 = self.init_1
        X2 = self.init_2
        #Handling the division by zero
        if not (self.fun(X1) - self.fun(X2)) :
            return "The initial values caused division By Zero"
        #The iterations
        while(iterations <= self.max_iterations):
            #no round
            if(self.precision == 0):
                Xnew = X2 - self.fun(X2) * (X1 - X2) / (self.fun(X1) - self.fun(X2))
            #round
            else:
                Xnew = round(X2 - self.fun(X2) * (X1 - X2) / (self.fun(X1) - self.fun(X2)), self.precision)
            Ea = abs((Xnew - X2) / Xnew) * 100
            print("X = ", Xnew, ", Ea = ", Ea, "%")
            X1 = X2
            X2 = Xnew
            iterations += 1
            #Convergence condition
            if(Ea < self.eps):
                time = timer() - begin_time
                criteria = "Converged"
                return [Xnew, iterations, criteria, time]
        #the method diverged
        time = timer() - begin_time
        criteria = "MAXIMUM ITERATIONS REACHED!!"
        return [Xnew, iterations, criteria, time]

#debugging
x=symbols('x')
fx = x**2 -2
print(fx)
secant = Secant(10**-20, 5, 0, 0.5, 1, fx)
print(secant.solve())