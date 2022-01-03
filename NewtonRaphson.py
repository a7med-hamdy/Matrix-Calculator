from sympy import *
from sigfig import round
from timeit import default_timer as timer

class NewtonRaphson:

    """
    constructor
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
    """
    def solve(self):
        begin_time = timer() #measure the execution time
        criteria = ""
        Ea = 100
        iterations = 0
        Xold = self.initValue
        #Handling the division by zero
        if(not self.fun_prime(Xold)):
            return "The initial value caused division By Zero"
        #The iterations
        while(iterations <= self.max_iterations):
            Xnew = round(Xold - self.fun(Xold) / self.fun_prime(Xold), sigfigs = self.precision)
            Ea = abs((Xnew - Xold) / Xnew) * 100
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
        criteria = "MAXIMUM ITERATIONS REACHED!!"
        return [Xnew, iterations, criteria, time, self.f_prime]

#debugging
# x=symbols('x')
# fx =  x**3 - 0.165*x**2 + 3.993*10**-4
# print(fx)
# newton = NewtonRaphson(10**-8, 8, None, 0.05, fx)
# print(newton.solve())