import numpy as np
import time
from sigfig import round

class LU_decomposer:
    matrix = np.array #coefficient matrix
    n = 0 #length of the matrix
    precision = 0 # percision number of significant figures
    vectorB = [] # the b vector 
    def __init__(self,x,tol,b):
        self.matrix = x
        self.n = x.shape[0]
        self.precision = tol
        self.vectorB = b

    def decompose(self, type):
        iterations = 0
        start = time.perf_counter()
        if(type == 1):
            lower,upper,identity = self.DollitleDecompose()
            self.vectorB = np.matmul(identity,self.vectorB)
            iterations += self.n**3/3
        elif(type == 3):
            a=np.array(self.matrix,float)
            if(not self.check_positive(a) or not self.check_symmetric(a)):
                return "not valid cholesky"
            else:
                lower, upper = self.CholeskyDecompose()
                iterations += self.n**3/6
        elif(type == 2):
            lower,upper = self.CroutDecompose()
            iterations += self.n**3/3
        else:
            return "invalid decomposition type"
        x = self.subistitute(upper,lower)
        iterations += self.n*(self.n-1)/2+self.n-1+self.n**3/3
        end = time.perf_counter()
        if(isinstance(x, str)):
            return x
        else :
            return [x, end-start, iterations]

    ## functiont to check that the array is Symitric
    def check_symmetric(self,a, rtol=1e-05, atol=1e-08):
        return np.allclose(a, a.T, rtol=rtol, atol=atol)


    ## functiont to check that the array is postive definte
    def check_positive(self,x):
        for i in np.linalg.eigvals(x):
            if i<0:
                return False
        return True

    ## cholesky decompostoin function
    def CholeskyDecompose(self):
        a=np.array(self.matrix,float)
        L=np.zeros_like(a, float)
        for j in range(self.n):
            for i in range(j,self.n):
                if(i==j):
                    summ=0
                    for l in range(j):
                        summ = round(summ+ L[i,l]**2 , self.precision)
                    L[i,j] = round(np.sqrt(a[i,j]-summ), self.precision)
                else:
                    summ=0
                    for l in range(j):
                        summ=round(summ+L[i,l]*L[j,l], self.precision) 
                    L[i,j]=round(round(a[i,j]-summ, self.precision)/L[j,j], self.precision)            
        return (L,L.T)        

    def CroutDecompose(self):
        Lower = []
        Upper = []
        sum = 0
        #do not decompose if matrix is not square
        coeffArray = self.matrix.tolist()
        for i in range(len(coeffArray)):
            Lower.append([0 for i in range(len(coeffArray))])
            Upper.append([0 for i in range(len(coeffArray))])
            if len(coeffArray[i]) != len(coeffArray):
                return "Error, not a square matrix"
        
        n = len(coeffArray)

        for j in range(len(coeffArray)):
            Upper[j][j] = 1             
            for i in range(j, len(coeffArray)):  
                sum = coeffArray[i][j]
                for k in range(j):
                    sum -= Lower[i][k]*Upper[k][j]
                Lower[i][j] = sum
            for i in range(j+1, len(coeffArray)):
                sumU = float(coeffArray[j][i])
                for k in range(j):
                    sumU -= Lower[j][k]*Upper[k][i]

                Upper[j][i] = sumU/Lower[j][j]

        array = np.dot(Lower,Upper)
        return np.array(Lower,np.float64),np.array(Upper,np.float64)

    
    def DollitleDecompose(self):
        scaling  = []
        identity = np.identity(self.n)
        for i in range(self.n):
            scaling.append(abs(self.matrix[i,0]))
            for j in range(1,self.n):
                if(abs(self.matrix[i,j]) > scaling[i]):
                    scaling[i] = abs(self.matrix[i,j])
        lower = np.zeros((self.n,self.n), np.float64)
        for k in range(0,self.n-1):
            lower,self.matrix,identity = self.pivot(scaling,k,identity,self.matrix, lower)
            for i in range(k+1,self.n):
                factor = round(self.matrix[i,k]/self.matrix[k,k], self.precision)
                lower[i,k] = factor
                for j in range(k,self.n):
                    self.matrix[i,j] = round(self.matrix[i,j]-round(factor*self.matrix[k,j], self.precision), self.precision)
        np.fill_diagonal(lower,1)
        return lower,self.matrix,identity

    def pivot(self,scaling,k,identity,upper,lower):
        pos = k
        biggest = (abs(upper[k][k]) / scaling[k], self.precision)
        for i in range(k+1,self.n):
            temp =  (abs(upper[i][k]) / scaling[i], self.precision)
            if(temp > biggest):
                biggest = temp
                pos = i
        if(pos != k): 
            upper[[pos,k]] = upper[[k,pos]]
            identity[[pos,k]] = identity[[k,pos]]
            lower[[pos,k]] = lower[[k,pos]]
        return lower,upper,identity

    def solutionsChecker(self, matrix, vector):
        z = np.all(matrix == 0, axis = 1)
        z = z.tolist()
        for i in z:
            if(z[i] == True):
                if(vector[i] == 0):
                    return 0
                else:
                    return 1
        return 2
    def subistitute(self,upper,lower):
        #forward subistitution
        value = self.solutionsChecker(lower, self.vectorB)
        if(value == 0):
            return "infinite solutions"
        elif(value == 1):
            return "no solution"
        y = [0]*self.n
        y[0] = round(self.vectorB[0]/lower[0,0], self.precision)
        for i in range(1,self.n):
            sum = self.vectorB[i]
            j = 0
            for j in range(i):
                sum = round(sum - round(lower[i,j]*y[j], self.precision), self.precision)
            y[i] = sum / lower[i,j+1]
        #backward subistitution
        value = self.solutionsChecker(upper, y)
        if(value == 0):
            return "infinite solutions"
        elif(value == 1):
            return "no solution"
        x = [0]*self.n
        x[self.n-1] = round(y[self.n-1] / upper[self.n-1,self.n-1], self.precision)
        i = self.n-1
        while(i >= 0):
            sum = 0
            for j in range (i+1,self.n):
                sum = round(sum + round(upper[i,j] * x[j], self.precision), self.precision)
            x[i] = round(round((y[i] - sum),self.precision)/ upper[i,i], self.precision)
            i-=1
        return x


