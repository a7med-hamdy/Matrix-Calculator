from Jacobi_Seidel.Jacobi_method import jacobiSolver
from Jacobi_Seidel.Seidel_method import SeidelSolver
import Jacobi_method,Seidel_method

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
            coeffArray[i].append(self.arrayB[i])
        
        if self.method == 4:    
            SeidSolver = SeidelSolver(coeffArray,self.iterMax,self.initalGuess,self.errorStop,self.significantFigs)
            return SeidSolver.Solve()
        if self.method ==5:
            JacSolver = jacobiSolver(coeffArray,self.iterMax,self.initalGuess,self.errorStop,self.significantFigs)
            return JacSolver.Solve()
        