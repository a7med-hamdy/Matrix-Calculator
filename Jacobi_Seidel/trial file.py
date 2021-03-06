import Jacobi_method
import Seidel_method
import IterativeSolver
coeffarray = [[5.0 , 10.0,-7.0], [7.0, 3.0, 8.0], [9.0, 10.0,-4.0]]
numofvar = 3
iterMax = 10
initalguess = [1,1,1]
errorStop = 10**-2
#jsolver = Jacobi_method.jacobiSolver(coeffarray,iterMax,initalguess,errorStop,5)
print('Jacobi answer\n')
#jsolver.Solve()
#print("=========================================\n")

#seidSolver = Seidel_method.SeidelSolver(coeffarray,iterMax,initalguess,errorStop,5)
#print('Seidel answer\n')

#seidSolver.Solve()
print("=========================================\n")
itersolve = IterativeSolver.iterSolver(coeffarray,[5,20,10],iterMax,initalguess,errorStop,5,5)

#itersolve.Solve()
#itersolve = IterativeSolver.iterSolver(coeffarray,[3,9,9],iterMax,initalguess,errorStop,5,4)
itersolve.Solveit()
