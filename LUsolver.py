class LUsolver:
    def __init__(self, L, U, B):
        self.L = L
        self.U = U
        self.vectorB = B
    
    #LU substitution method
    #return: solution vector x[]
    def LU_solver(self):
        #LUx = B , Ux = c
        n = len(self.L)
        x = [0] * n
        c = [0] * n

        #Forward substitution
        #solve: Lc = B
        c[0] = self.vectorB[0] / self.L[0][0]
        for i in range(1, n):
            # iterations += 1
            sum = 0
            for j in range(0, i):
                # iterations += 1
                sum = sum + self.L[i][j] * c[j]
            c[i] = (self.vectorB[i] - sum) / self.L[i][i]

        #Backward substitution
        #solve: Ux = c
        x[-1] = c[-1] / self.U[-1][-1]
        for i in range(n-2, -1, -1):
            # iterations += 1
            sum = 0
            for j in range(i+1, n):
                # iterations += 1
                sum = sum + self.U[i][j] * x[j]
            x[i] = (c[i] - sum) / self.U[i][i]
        return x
#debugging
print(LUsolver([[1,0,0], [1,1,0], [2,-1/3,1]],
               [[1,1,-1], [0,-3,4], [0,0,13/3]], [4,-6,7]).LU_solver())