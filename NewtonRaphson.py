import math
from tkinter.constants import X
from sympy import *
from sigfig import round
from timeit import default_timer as timer

class NewtonRaphson:

    """
    constructor
    @param: (eps) the stopping approximate absolute error
    @param: (max_iterations)
    @param: (precision)
    @param: (initValue) the initial value
    @param: (fun) the equation 'f(x)'
    """
    def __init__(self, eps, max_iterations, precision, initValue, fun):
        self.eps = eps
        self.max_iterations = max_iterations
        self.precision = precision
        self.initValue = initValue
        self.x = Symbol('x')
        self.fun = lambdify(self.x, fun)
        self.f_prime = fun.diff(self.x)
        self.fun_prime = lambdify(self.x, fun.diff(self.x))

    """
    solve function 
    @return: array that consists of:
            1. (Xnew) the root found.
            2. (iterations) the number of iterations taken.
            3. (criteria) either "Converged" or "Diverged"
                              or "The initial value caused division By Zero".
            4. (time) the time that the algorithm takes to slove.
            5. (f_prime) the derivative of f(x) -> "f'(x)"
    """
    def solve(self):
        begin_time = timer() #measure the execution time
        criteria = ""
        Ea = 100
        iterations = 0
        Xold = self.initValue
        #The iterations
        while(iterations < self.max_iterations):
            #Handling the division by zero
            if(self.fun_prime(Xold) == 0):
                time = timer() - begin_time
                criteria = "The initial value caused \ndivision By Zero"
                return [Xold, iterations, criteria, time, self.f_prime]
            Xnew = Xold - self.fun(Xold) / self.fun_prime(Xold)
            if math.isnan(Xnew):
                break
            Xnew = round(Xnew, sigfigs = self.precision)
            #if Xnew == zero Then do NOT calculate the error
            if(Xnew != 0):
                Ea = abs((Xnew - Xold) / Xnew) * 100
            else:
                print("X = ", Xnew, ", Ea = ", Ea, "%")
                Xold = Xnew
                iterations += 1
                continue
            print("X = ", Xnew, ", Ea = ", Ea, "%")
            Xold = Xnew
            iterations += 1
            #Convergence condition
            if(Ea < self.eps):
                time = timer() - begin_time
                criteria = "Converged"
                return [Xnew, iterations, criteria, time, self.f_prime]
        #the method diverged
        time = timer() - begin_time
        criteria = "Diverged"
        return [Xnew, iterations, criteria, time, self.f_prime]

#debugging
# x=symbols('x')
# fx =  ln(x)+1
# print(fx)
# newton = NewtonRaphson(10**-8, 50, 5, 1, fx)
# print(newton.solve())