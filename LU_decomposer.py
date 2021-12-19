import numpy as np
class LU_decomposer:
    _matrix = np.array
    def show(self):
        print(self._matrix)
    def set_matrix(self,x):
        self._matrix = x
    def LU(self,a,b,n,tol):
        p = np.identity(n)
        s = []
        x = [0]*n
        l,u = self.decompose(a,n,tol,b,s,p)
        b = np.matmul(p,b)
        print(np.matmul(l,u))
        print(self.subistitute(u,l,n,b,x))
    def decompose(self,a, n,tol,b,s,p):
        for i in range(n):
            s.append(abs(a[i,0]))
            for j in range(1,n):
                if(abs(a[i,j]) > s[i]):
                    s[i] = abs(a[i,j])
        z = np.zeros((n,n), np.float64)
        for k in range(0,n-1):
            self.pivot(a,b,s,n,k,p)
            z = np.matmul(p,z)
            for i in range(k+1,n):
                factor = a[i,k]/a[k,k]
                z[i,k] = factor
                for j in range(k,n):
                    a[i,j] -= factor*a[k,j]
        print(z)
        np.fill_diagonal(z,1)
        return z,a
    def pivot(self,a,b,s,n,k,l):
        p = k
        b = abs(a[k,k]) / s[k]
        for i in range(k+1,n):
            temp =  abs(a[i,k]) / s[i]
            if(temp > b):
                b = temp
                p = i
        if(p != k): 
            a[[p,k]] = a[[k,p]]
            l[[p,k]] = l[[k,p]]
            

    def subistitute(self,a,z,n,b,x):
        print(b)
        y = [0]*n
        y[0] = b[0]
        for i in range(1,n):
            sum = b[i]
            for j in range(0,i):
                q = sum
                sum -= z[i,j]*y[j]
                print(f'{j},{sum} = {q} - {z[i,j]} * {y[j]}')
            y[i] = sum
        print(y)
        x[n-1] = y[n-1] / a[n-1,n-1]
        i = n-1
        while(i >= 0):
            sum = 0
            for j in range (i+1,n):
                sum = sum + a[i,j] * x[j]
            x[i] = (y[i] - sum) / a[i,i]
            i-=1
        return x



def main():
    x = LU_decomposer()
    x.set_matrix(np.array([4,5]))
    x.show()
    x.LU(np.array([[25,5,1],[64,8,1],[144,12,1]], np.float64),[106.8,177.2,279.2],3,1)
if __name__ == "__main__":
    main()