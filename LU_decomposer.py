import numpy as np
import time
from sigfig import round

class LU_decomposer:
    matrix = np.array #coefficient matrix
    n = 0 #length of the matrix
    precision = 0 # percision number of significant figures
    vectorB = [] # the b vector 
    iteration_counter = 0
    def __init__(self,x,tol,b):
        self.matrix = x
        self.n = x.shape[0]
        self.precision = tol
        self.vectorB = b

    def decompose(self, type):
        start = time.perf_counter()
        self.iteration_counter = 0
        if(type == "dolittle"):
            lower,upper,identity = self.DollitleDecompose()
            self.vectorB = np.matmul(identity,self.vectorB)
        elif(type == "cholesky"):
            self.CholeskyDecompose()
        elif(type == "crout"):
            lower,upper = self.CroutDecompose()
        else:
            lower, upper = print("invalid decomposition type")
        end = time.perf_counter()
        print(np.matmul(lower,upper))
        print(f'execution time for decomposition : {end-start}')
        print(self.subistitute(upper,lower))

    ## functiont to check that the array is Symitric
    def check_symmetric(self,a, rtol=1e-05, atol=1e-08):
        return np.allclose(a, a.T, rtol=rtol, atol=atol)


    ## functiont to check that the array is postive definte
    def check_positive(self,x):
        for i in np.linalg.eigvals(x):
            if i>0:
                return False
            return True

    ## cholesky decompostoin function
    def CholeskyDecompose(self):
        a=np.array(self.matrix,float)
        if(not self.check_positive(a) or not self.check_symmetric(a)):
            print("not valid cholesky")
            return 
        L=np.zeros_like(a)
        z=0
        for j in range(self.n):
                
            for i in range(j,self.n):
                if i==j:
                    summ=0
                    for l in range(j):
                        summ = round(summ+ L[i,l]**2 , self.precision)
                        z+=1
                            
                        L[i,j] = round(np.sqrt(a[i,j]-summ), self.precision)
                        
                else:
                    summ=0
                    for l in range(j):
                        summ=round(summ+L[i,l]*L[j,l], self.precision)
                        z+=1
                            
                    L[i,j]=round(round(a[i,j]-summ, self.precision)/L[j,j], self.precision)
                        
        

    def CroutDecompose(self):
        lower = []
        upper = []
        sum = 0
        #do not decompose if matrix is not square
        the_list = self.matrix.tolist()
        for i in range(len(the_list)):
            lower.append([0 for i in range(len(the_list))])
            upper.append([0 for i in range(len(the_list))])
            if len(the_list[i]) != len(the_list):
                return "Error, not a square matrix"

        for i in range(0, len(the_list)):
            upper[i][i]  = 1
            sum = 0
            for j in range(i, len(the_list)):
                for k in range(0, i):
                    sum += round(lower[j][k] * upper[k][i], self.precision)
                lower[j][i] = round(the_list[j][i] - sum, self.precision) 
            sum = 0
            for j in range(i+1, len(the_list)):
                for k in range(0, i):
                    sum += round(lower[i][k] * upper[k][j], self.precision) 
                upper[i][j] = round((the_list[i][j] - sum) / lower[i][i], self.precision)

        return np.array(upper,np.float64),np.array(lower,np.float64)

    
    def DollitleDecompose(self):
        scaling  = []
        identity = np.identity(self.n)
        for i in range(self.n):
            scaling.append(abs(self.matrix[i,0]))
            for j in range(1,self.n):
                self.iteration_counter +=1
                if(abs(self.matrix[i,j]) > scaling[i]):
                    scaling[i] = abs(self.matrix[i,j])
        lower = np.zeros((self.n,self.n), np.float64)
        for k in range(0,self.n-1):
            lower,self.matrix,identity = self.pivot(scaling,k,identity,self.matrix, lower)
            for i in range(k+1,self.n):
                factor = round(self.matrix[i,k]/self.matrix[k,k], self.precision)
                lower[i,k] = factor
                for j in range(k,self.n):
                    self.iteration_counter +=1
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

    def subistitute(self,upper,lower):
        #forward subistitution
        y = [0]*self.n
        y[0] = round(self.vectorB[0], self.precision)
        for i in range(1,self.n):
            sum = self.vectorB[i]
            for j in range(0,i):
                sum = round(sum - round(lower[i,j]*y[j], self.precision), self.precision)
            y[i] = sum
        #backward subistitution
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



def main():
    x = LU_decomposer(np.array([[25,5,1],[64,8,1],[144,12,1]], np.float64),20,[106.8,177.2,279.2])
    x.decompose("cholesky")
if __name__ == "__main__":
    main()