from Jacobi_Seidel import Jacobi_method 
from Jacobi_Seidel import Seidel_method

class iterSolver:

    def __init__(self, coArray,  arrayB,iterMax, initalGuess, errorStop,significantFigs,method):
        self.coArray = coArray
        self.arrayB = arrayB
        self.iterMax = iterMax
        self.initalGuess = initalGuess
        self.errorStop = errorStop
        self.significantFigs = significantFigs
        self.method = method
    
    def Solve(self):
        i = 0
        coeffArray = self.coArray
        while i < len(coeffArray):
            print("hello")
            coeffArray[i].append(self.arrayB[i])
            i += 1
        
        if self.method == 4:    
            SeidSolver = Seidel_method.SeidelSolver(coeffArray,self.iterMax,self.initalGuess,self.errorStop,self.significantFigs)
            return SeidSolver.Solve()
        if self.method ==5:
            JacSolver = Jacobi_method.jacobiSolver(coeffArray,self.iterMax,self.initalGuess,self.errorStop,self.significantFigs)
            return JacSolver.Solve()
        