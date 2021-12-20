import Pivoting
from sigfig import round

def Forward_Elimination(n, A, B, precision, iterations):
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
                return A, B, -1 #send -1 iterations as an evidence
            for k in range(i, n):
                iterations += 1
                A[j][k] = round(A[j][k] - factor * A[i][k], sigfigs = precision)
            B[j] = round(B[j] - factor * B[i], sigfigs = precision)
    return A, B, iterations