import Jacobi_method
import Seidel_method
import IterativeSolver
coeffarray = [[1.0, 23.0, 2.0],
 [1.0, 12.0, 1.0],
  [13.0, 1.0, 2.0]]
numofvar = 3
iterMax = 100
initalguess = [1,1,1]
errorStop = 10**(-1)
#jsolver = Jacobi_method.jacobiSolver(coeffarray,iterMax,initalguess,errorStop,5)
#print('Jacobi answer\n')
#jsolver.Solve()
#print("=========================================\n")

#seidSolver = Seidel_method.SeidelSolver(coeffarray,iterMax,initalguess,errorStop,5)
#print('Seidel answer\n')

#seidSolver.Solve()
print("=========================================\n")
itersolve = IterativeSolver.iterSolver(coeffarray,[3,9,9],iterMax,initalguess,errorStop,5,5)

itersolve.Solve()
itersolve = IterativeSolver.iterSolver(coeffarray,[3,9,9],iterMax,initalguess,errorStop,5,4)
itersolve.Solve()
