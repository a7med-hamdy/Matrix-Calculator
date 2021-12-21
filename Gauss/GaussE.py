from ForwardE import Forward_Elimination
from Scaling import scaling
from sigfig import round
from timeit import default_timer as timer
#Gauss Elimination:
#   Forward Elimination
#   Backward Substitution
epsilon = 10**-5
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
        #Scaling
        A, B = scaling(n, A, B, precision)
        #Forward Elimination
        A, B, iterations = Forward_Elimination(n, A, B, precision, iterations)
        
        if(iterations == -1): #if dividing by zero occurs that means -> infinite solutions (variable eliminated) 
            return "The system has infinite number of solutions"
      
        #Check if the system has no unique solution
        if(abs(A[-1][-1]) < epsilon):    
            if( abs(B[-1]) < epsilon ):
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
        #print('X = ', X)
        #print("Time = %.10s seconds" % time)
        #print('Number of iterations = ', iterations)
        return [X, time ,iterations ]
    #End solve

#debugging
# print(GaussE().solve(3, [[2,1,4],
#                          [1,2,3],
#                          [4,-1,2]], [1,1.5,2], 3)) #unique solution
# print('------------------------------------------------------------')
# print(GaussE().solve(3, [[2,1,4],
#                          [4,2,8],
#                          [1,0.5,2]], [1,2,0.5], 3)) #infinite solutions
