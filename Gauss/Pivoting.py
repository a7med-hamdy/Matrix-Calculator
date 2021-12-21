#Partial pivoting function
##@param n: the size of the coefficients matrix (square)
##@param p: the index of the pivot
##@param a: the coefficients matrix
##@param b: the constants vector
#@return a, b
def pivoting(n, p, a, b):

    #finding the index of the maximum absolude value below the pivot
    max_index = p
    for i in range(p+1, n):
        if abs(a[max_index][p]) < abs(a[i][p]):
            max_index = i
    #swap the two rows in A & B matrices
    temp = 0
    if(max_index != p):
        #A - the coefficients matrix
        for i in range(0, n):
            temp = a[p][i]
            a[p][i] = a[max_index][i]
            a[max_index][i] = temp
        #B - the constants matrix
        temp = b[p]
        b[p] = b[max_index]
        b[max_index] = temp
    
    return a, b
#End pivoting

#debugging
# print(pivoting(3, 0,[[-6,2,3],
#                      [-18,5,6],
#                      [-7,8,9]], [1,2,3]))