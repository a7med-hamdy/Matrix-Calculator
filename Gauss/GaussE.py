import Pivoting
from sigfig import round
from timeit import default_timer as timer
#Gauss Elimination:
#   Forward Elimination
#   Backward Substitution

class GaussE():
    #@param n: the size of the coefficients matrix (square)
    #@param A: the coefficients matrix
    #@param B: the constants vector
    #@param precision: the required precision
    #return if(unique solution) -> [ X[]:solution, iteraions, Time ]
    #       if(no solution) -> "The system has no solution"
    #       if(infinite sol.) -> "The system has infinite number of solutions"       
    def solve(self,n, A, B, precision = 5):
        begin_time = timer() #measure the execution time
        iterations = 0 #number of iterations counter
        #Forward Elimination
        factor = 0
        for i in range(n-1):
            iterations += 1
            A, B = Pivoting.pivoting(n, i, A, B) #search for pivoting in each iteration
            for j in range(i+1, n):
                iterations += 1
                #if dividing by zero occurs that means -> infinite solutions (variable eliminated)
                try:
                    factor = round(A[j][i] / A[i][i], sigfigs = precision)
                except:
                    return "The system has infinite number of solutions"
                for k in range(i, n):
                    iterations += 1
                    A[j][k] = round(A[j][k] - factor * A[i][k], sigfigs = precision)
                B[j] = round(B[j] - factor * B[i], sigfigs = precision)
        print(A, B)
        #Check if the system has no unique solution
        if(A[-1][-1] == 0):    
            if( B[-1] == 0 ):
                return "The system has infinite number of solutions"
            else:
                return "The system has no solution"
        X = [0] * n
        #Backward Substitution
        X[-1] = round(B[-1] / A[-1][-1], sigfigs = precision)
        for i in range(n-2, -1, -1):
            iterations += 1
            sum = 0
            for j in range(i+1, n):
                iterations += 1
                sum = round(sum + A[i][j] * X[j], sigfigs = precision)
            X[i] = round((B[i] - sum) / A[i][i], sigfigs = precision)
        time = timer() - begin_time
        print('X = ', X)
        print("Time = %.10s seconds" % time)
        print('Number of iterations = ', iterations)
        return [X, iterations, time]
    #End solve

#debugging
#print(GaussE.solve(3, [[2,1,4],
                       #[1,2,3],
                       #[4,-1,2]], [1,1.5,2], 3)) #unique solution
#print('------------------------------------------------------------')
#print(GaussE.solve(3, [[2,1,4],
                       #[4,2,8],
                       #[1,0.5,2]], [1,2,0.5], 3)) #infinite solutions
