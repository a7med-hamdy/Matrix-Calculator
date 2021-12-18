import Pivoting
#Gauss-Jordan:
#   Forward Elimination
#   Backward Elimination

class Gauss_Jordan():

    def init(self, n, A, B):
        self.n = n
        self.A = A
        self.B = B

    def solve(n, A, B):
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

        #Backward Elimination
        for i in range(n-1, 0, -1):
            iterations += 1
            for j in range(i-1, -1, -1):
                iterations += 1
                factor = A[j][i] / A[i][i]
                for k in range(i, -1, -1):
                    iterations += 1
                    A[j][k] = A[j][k] - factor * A[i][k]
                B[j] = B[j] - factor * B[i]
        print(A, B)
        X = [0] * n
        for i in range(n):
            iterations += 1
            X[i] = B[i] / A[i][i]
        print('X= ', X)
        print('number of iterations = ', iterations)
        return X

Gauss_Jordan.solve(3, [[2,1,4],
                       [1,2,3],
                       [4,-1,2]], [1,1.5,2])