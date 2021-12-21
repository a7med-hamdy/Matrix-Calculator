import numpy as np
from timeit import default_timer as timer
class jacobiSolver:

    def __init__(self, coArray,  iterMax, initalGuess, errorStop,significantFigs):
        self.coArray = coArray
        self.iterMax = iterMax
        self.initalGuess = initalGuess
        self.errorStop = errorStop
        self.significantFigs =  significantFigs
        
    #calculate new array of guesses from the previous guesses
    #
    # parameters :
    # 
    # prevGuess : previous guess array
    # 
    # 
    # returns :
    #
    # arr : newGuess array
    # 
    def __getGuesses(self,prevGuess):
        arr = []
        #loop in the coefficent array
        for i in range(len(self.coArray)):
            #get the last value (b)
            #if a diagonal element is zero pivot elements
            if self.coArray[i][i] == 0:
                self.__pivoting(i)

            last = self.coArray[i][len(self.coArray[i])-1]
            x = last
            #loop in each equation
            for j in range(len(self.coArray[i])-1):
                #skip a loop if the value is the coefficent of the variable being guessed
                if i == j:
                    continue
                else:
                    #calculate the new guess
                    x = x - (self.coArray[i][j] * prevGuess[j])
            x = x/self.coArray[i][i]
            #push the guess in its place 
            arr.append(x)

        return arr


    #Partial pivoting function
    ##@param p: the index of the pivot
    def __pivoting(self,p):
        #finding the index of the maximum value below the pivot
        n=len(self.coArray)
        max_index = p
        for i in range(p+1, n):
            if abs(self.coArray[max_index][p]) < abs(self.coArray[i][p]):
                max_index = i
        #swap the two rows in A matrix
        temp = 0
        if(max_index != p):
            for i in range(0, n):
                temp = self.coArray[p][i]
                self.coArray[p][i] = self.coArray[max_index][i]
                self.coArray[max_index][i] = temp
    #End pivoting




    #Solves systems of linear equations using Jacobi Iterations method
    # 
    # 
    # returns :
    #
    # guess : array of guesses of last iteration
    # 
    def Solve(self):
        i = 0 
        errorSatisCount = 0
        crit = ""
        #get the value of the inital guess
        guess = self.initalGuess
        time = 0
        while i < self.iterMax:
            begin_time = timer()
            #store the value of the previous guess
            prevGuess = guess
            #calculate the new guess using the old one
            guess = self.__getGuesses(prevGuess)
            guess = np.array(guess)
            #round the result
            #calculate the error
            error = abs(np.array(guess) - np.array(prevGuess)/np.array(guess))
            #check for divergence to avoid wasting runtime
            if np.inf in error:                
                time = timer() - begin_time
                crit = "Diverged"
                return guess.tolist(),crit,time
            elif np.inf in guess:
                time = timer() - begin_time
                crit = "Diverged"
                return guess.tolist(),crit,time


            error = error.round(self.significantFigs+1)
            guess  = guess.round(self.significantFigs)
            error = error.tolist()



            #compare with given error criteria
            for k in range(len(error)):
                if error[k] < self.errorStop:
                    errorSatisCount =errorSatisCount + 1
            i = i+1
            if i <= self.iterMax:
                print(guess, error, errorSatisCount,i)
            if i == self.iterMax:
                time = timer() - begin_time
            # if all values satisfy the criteria
            # stop iterating
            if errorSatisCount == len(error)+1:
                time = timer() - begin_time
                break
        #if check for more iterations if the value converges or diverges
        if(i == self.iterMax+1000):
            crit ="will Diverge"
        else:
            crit = "Will Converge"
        return guess.tolist(),crit,time

