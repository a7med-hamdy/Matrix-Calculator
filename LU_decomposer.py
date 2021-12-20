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
    #driver method that prefrom the decomposition based upon the type of operation
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
                #if the element is diagonal
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
    ## crout decompostoin function
    def CroutDecompose(self):
        #intialize lower and upper matrices
        Lower = []
        Upper = []
        sum = 0
        coeffArray = self.matrix.tolist()
        for i in range(len(coeffArray)):
            Lower.append([0 for i in range(len(coeffArray))])
            Upper.append([0 for i in range(len(coeffArray))])
        for j in range(len(coeffArray)):
            Upper[j][j] = 1  
            # form the lower matrix           
            for i in range(j, len(coeffArray)):  
                sum = coeffArray[i][j]
                for k in range(j):
                    sum = (sum-round(Lower[i][k]*Upper[k][j], self.precision), self.precision)
                Lower[i][j] = sum
            # form the upper matrix
            for i in range(j+1, len(coeffArray)):
                sumU = round(float(coeffArray[j][i]), self.precision)
                for k in range(j):
                    sumU = round(sumU - round(Lower[j][k]*Upper[k][i], self.precision), self.precision)
                Upper[j][i] = round(sumU/Lower[j][j], self.precision)
        return np.array(Lower,np.float64),np.array(Upper,np.float64)


    def DollitleDecompose(self):
        scaling  = [] # the list will hold teh largest element in each row for scaling
        identity = np.identity(self.n) #the identity matrix to swap teh rows in case of pivoting
        # append the elements in the scaling array
        for i in range(self.n):
            scaling.append(abs(self.matrix[i,0]))
            for j in range(1,self.n):
                if(abs(self.matrix[i,j]) > scaling[i]):
                    scaling[i] = abs(self.matrix[i,j])
        #intialize the lower array
        lower = np.zeros((self.n,self.n), np.float64)
        for k in range(0,self.n-1):
            # preform the pivoting
            lower,self.matrix,identity = self.pivot(scaling,k,identity,self.matrix, lower)
            for i in range(k+1,self.n):
                factor = round(self.matrix[i,k]/self.matrix[k,k], self.precision)
                lower[i,k] = factor
                for j in range(k,self.n):
                    self.matrix[i,j] = round(self.matrix[i,j]-round(factor*self.matrix[k,j], self.precision), self.precision)
        np.fill_diagonal(lower,1)
        return lower,self.matrix,identity
    #a function that preforms pivoting
    def pivot(self,scaling,k,identity,upper,lower):
        pos = k
        biggest = (abs(upper[k][k]) / scaling[k], self.precision)
        for i in range(k+1,self.n):
            # if there is a larger element make it the largest one and save the index
            temp =  (abs(upper[i][k]) / scaling[i], self.precision)
            if(temp > biggest):
                biggest = temp
                pos = i
        # if the largest element changed swap
        if(pos != k): 
            upper[[pos,k]] = upper[[k,pos]]
            identity[[pos,k]] = identity[[k,pos]]
            lower[[pos,k]] = lower[[k,pos]]
        return lower,upper,identity
    #helper method to check for infinite or no solutions
    def solutionsChecker(self, matrix, vector):
        z = np.all(matrix == 0, axis = 1)
        z = z.tolist()
        for i in z:
            if(z[i] == True):
                if(vector[i] == 0):
                    return 0 #for infinite solutions
                else:
                    return 1  # for no solutions
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


