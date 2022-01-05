import math
from sympy import *
from sigfig import round
from timeit import default_timer as timer

class Secant:

    """
    constructor
    @param: (eps) the stopping approximate absolute error
    @param: (max_iterations)
    @param: (precision)
    @param: (init_1) the 1st initial value
    @param: (init_2) the 2nd initial value
    @param: (fun) the equation 'f(x)'
    """
    def __init__(self, eps, max_iterations, precision, init_1, init_2, fun):
        self.eps = eps
        self.max_iterations = max_iterations
        self.precision = precision
        self.init_1 = init_1
        self.init_2 = init_2
        self.x = Symbol('x')
        self.f_prime = fun.diff(self.x)
        self.fun = lambdify(self.x, fun)

    """
    solve function
    @return: array that consists of:
            1. (Xnew) the root found.
            2. (iterations) the number of iterations taken.
            3. (criteria) either "Converged" or "Diverged"
                              or "The initial values caused division By Zero".
            4. (time) the time that the algorithm takes to slove.
            5. (f_prime) the derivative of f(x) -> "f'(x)"
    """
    def solve(self):
        begin_time = timer() #measure the execution time
        criteria = ""
        Ea = 100
        iterations = 0
        X1 = self.init_1
        X2 = self.init_2
        #The iterations
        while(iterations < self.max_iterations):
            #Handling the division by zero
            if(self.fun(X1) == self.fun(X2)):
                time = timer() - begin_time
                criteria = "The initial values caused \ndivision By Zero"
                return [X2, iterations, criteria, time, self.f_prime]
            Xnew = X2 - self.fun(X2) * (X1 - X2) / (self.fun(X1) - self.fun(X2))
            if math.isnan(Xnew):
                break
            Xnew = round(Xnew, sigfigs = self.precision)
            #if Xnew == zero (division by zero)
            if(Xnew != 0):
                Ea = abs((Xnew - X2) / Xnew) * 100
            else:
                print("X = ", Xnew, ", Ea = ", Ea, "%")
                X1 = X2
                X2 = Xnew
                iterations += 1
                continue
            print("X = ", Xnew, ", Ea = ", Ea, "%")
            X1 = X2
            X2 = Xnew
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
# fx = exp(x)+x
# print(fx)
# secant = Secant(10**-20, 50, None, -9, 2, fx)
# print(secant.solve())