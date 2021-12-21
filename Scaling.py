from sigfig import round
#Scaling function
##@param n: the size of the coefficients matrix (square)
##@param a: the coefficients matrix
##@param b: the constants vector
#@return a, b

def scaling(n, a, b, precision):
    #for each  row
    for i in range(0, n):
        max_index = 0
        #searching for the largest magnitude of the coefficients in current row
        for j in range(1, n):
            if(abs(a[i][max_index]) < abs(a[i][j])):
                max_index = j
        #dividing the entire row by the largest coefficient
        for k in range(0, n):
            if(k != max_index):
                a[i][k] = round(a[i][k] / a[i][max_index], sigfigs = precision)
        b[i] = round(b[i] / a[i][max_index], sigfigs = precision)
        a[i][max_index] = 1
    return a, b
#End scaling


#debugging
# print(scaling(2, [[1,1],[2,100000]], [2,100000], 3))