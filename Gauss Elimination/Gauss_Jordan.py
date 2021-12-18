import Pivoting
from sigfig import round
from timeit import default_timer as timer
#Gauss-Jordan:
#   Forward Elimination
#   Backward Elimination

class Gauss_Jordan():

    def solve(n, A, B, precision = 5):
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
        #Check if the system has no unique solution
        if(A[-1][-1] == 0):    
            if( B[-1] == 0 ):
                return "The system has infinite number of solutions"
            else:
                return "The system has no solution"
        #Backward Elimination
        for i in range(n-1, 0, -1):
            iterations += 1
            for j in range(i-1, -1, -1):
                iterations += 1
                factor = round(A[j][i] / A[i][i], sigfigs = precision)
                for k in range(i, -1, -1):
                    iterations += 1
                    A[j][k] = round(A[j][k] - factor * A[i][k], sigfigs = precision)
                B[j] = round(B[j] - factor * B[i], sigfigs = precision)
        print(A, B)
        #substitution
        X = [0] * n
        for i in range(n):
            iterations += 1
            X[i] = round(B[i] / A[i][i], sigfigs = precision)
        time = round(timer() - begin_time, sigfigs = precision)
        print('X= ', X)
        print("-> %s seconds <-" % time)
        print('number of iterations = ', iterations)
        return X, iterations, time
    #End solve

#debugging
print(Gauss_Jordan.solve(3, [[2,1,4],
                             [1,2,3],
                             [4,-1,2]], [1,1.5,2], 5)) #unique solution
print('-----------------------------------------------------------')
print(Gauss_Jordan.solve(3, [[1,1,1],
                             [0,1,-3],
                             [2,1,5]], [2,1,0], 3)) #no solution