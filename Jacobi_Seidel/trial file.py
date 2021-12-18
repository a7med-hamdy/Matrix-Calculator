import Jacobi_method
import Seidel_method
coeffarray = [
[0, 3, 5,3],
[1, 0, 3,9],
[3, 7, 0,9]] 
numofvar = 3
iterMax = 100
initalguess = [1,1,1]
errorStop = 10**(-1)
jsolver = Jacobi_method.jacobiSolver(coeffarray,iterMax,initalguess,errorStop,5)
print('Jacobi answer\n')
jsolver.Solve()
print("=========================================\n")

seidSolver = Seidel_method.SeidelSolver(coeffarray,iterMax,initalguess,errorStop,5)
print('Seidel answer\n')

seidSolver.Solve()