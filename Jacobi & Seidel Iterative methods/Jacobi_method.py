import numpy as np
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
        #get the value of the inital guess
        guess = self.initalGuess
        while i < self.iterMax:
            #store the value of the previous guess
            prevGuess = guess
            #calculate the new guess using the old one
            guess = self.__getGuesses(prevGuess)
            guess = np.array(guess)
            #round the result
            guess  = guess.round(self.significantFigs)
            #calculate the error
            error = abs(np.array(guess) - np.array(prevGuess)/np.array(guess))
            error = error.round(self.significantFigs+1)
            error = error.tolist()

            #compare with given error criteria
            for k in range(len(error)):
                if error[k] < self.errorStop:
                    errorSatisCount =errorSatisCount + 1
            i = i+1
            if i <= self.iterMax:
                print(guess, error, errorSatisCount,i)
            # if all values satisfy the criteria
            # stop iterating
            if errorSatisCount == len(error)+1:
                break
        #if check for more iterations if the value converges or diverges
        if(i == self.iterMax+1000):
            print("will Converge")
        else:
            print("Will Diverge")
        return guess

