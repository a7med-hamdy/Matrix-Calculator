import Pivoting
import time as t
#Gauss Elimination:
#   Forward Elimination
#   Backward Substitution

class Gauss_Elimination():
    #constructor
    def init(self, n, A, B):
        self.n = n
        self.A = A
        self.B = B

    #solving function
    def solve(n, A, B):
        begin_time = t.time() #measure the execution time
        iterations = 0 #number of iterations counter
        #Forward Elimination
        factor = 0
        for i in range(n-1):
            iterations += 1
            A, B = Pivoting.pivoting(n, i, A, B) #search for pivoting in each iteration
            for j in range(i+1, n):
                iterations += 1
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    iterations += 1
                    A[j][k] = A[j][k] - factor * A[i][k]
                B[j] = B[j] - factor * B[i]
        print(A, B)
        X = [0] * n
        #Backward Substitution
        X[-1] = B[-1] / A[-1][-1]
        for i in range(n-2, -1, -1):
            iterations += 1
            sum = 0
            for j in range(i+1, n):
                iterations += 1
                sum = sum + A[i][j] * X[j]
            X[i] = (B[i] - sum) / A[i][i]
        print("---> %s seconds <---" % (t.time() - begin_time))
        print('X = ', X)
        print('number of iterations = ', iterations)
        return X

#debugging
Gauss_Elimination.solve(3, [[2,1,4],
                            [1,2,3],
                            [4,-1,2]], [1,1.5,2])