import numpy as np
from timeit import default_timer as timer
import sigfig
import copy
class iterSolver:

    def __init__(self, coArray,  arrayB,iterMax, initalGuess, errorStop,significantFigs,method):
        self.coArray = coArray
        self.arrayB = arrayB
        self.iterMax = iterMax
        self.initalGuess = initalGuess
        self.errorStop = errorStop
        self.significantFigs = significantFigs
        self.method = method
  
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
    def __getGuessesJacobi(self,prevGuess):
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

    def __getGuessesSeidel(self,prevGuess):
        arr = []
        #loop in the coefficent array
        prev = copy.deepcopy(prevGuess)
        for i in range(len(self.coArray)):
            #get the last value (b)
            last = self.coArray[i][len(self.coArray[i])-1]
            prev[i] = last
            #loop in each equation
            for j in range(len(self.coArray[i])-1):
                #skip a loop if the value is the coefficent of the variable being guessed
                if i == j:
                    continue
                else:
                    #calculate the new guess
                    prev[i] = prev[i] - (self.coArray[i][j] * prev[j])
            prev[i] = prev[i]/self.coArray[i][i]
            #push the guess in its place 
            arr.append(prev[i])

        return arr


    #Solves systems of linear equations using Jacobi/Seidel Iterations method
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
        guessLast = guess
        time = 0
        #################################loopbody start#############################################
        while i < self.iterMax+1000:
            begin_time = timer()
            #store the value of the previous guess
            prevGuess = copy.deepcopy(guess)
            errorSatisCount = 0
            #calculate the new guess 
            try:
                if self.method == 4:
                    guess = self.__getGuessesSeidel(prevGuess)
                elif self.method == 5:
                    guess = self.__getGuessesJacobi(prevGuess)
            except:
                guessLast = copy.deepcopy(guess)
                time = timer() - begin_time
                crit = "Division by zero!"
                return crit
            #calculate the error
            error = (abs(np.array(guess) - np.array(prevGuess)))

            error = error.tolist()

            #compare with given error criteria
            for k in range(len(error)):
                if error[k] < self.errorStop:
                    errorSatisCount = errorSatisCount + 1
    
            #increment counter
            i = i+1

            #round guess and check for divergence
            if i <= self.iterMax:
                try:
                    #round guess
                    for j in range(0,len(guess)):
                        guess[j]  = sigfig.round(guess[j],sigfigs = self.significantFigs)
                except ValueError:
                    guessLast = copy.deepcopy(guess)
                    time = timer() - begin_time
                    crit = "Diverged!"
                    break

            #calculate time
            if i == self.iterMax:
                guessLast = copy.deepcopy(guess)
                time = timer() - begin_time

            # if all values satisfy the criteria
            # stop iterating
            if errorSatisCount == len(error):
                time = timer() - begin_time
                crit = "Converged!"
                break

        ################################loop body end#######################################
        #round last guess
        for j in range(0,len(guessLast)):
            guessLast[j]  = sigfig.round(guessLast[j],sigfigs = self.significantFigs)

        #if check for more iterations if the value converges or diverges
        if (i > self.iterMax):
            if(i == self.iterMax+1000):
                crit = "will Diverge"
                
            else:
                crit = "Will Converge"
            i = self.iterMax

        #check for divergence
        if (np.inf in error) or (np.inf in guess):                
                crit = "Diverged"
                return [guessLast,time,i,crit]

        return [guessLast,time,i,crit]





    def Solveit(self):
        i = 0
        while i < len(self.coArray):
            self.coArray[i].append(self.arrayB[i])
            i += 1
        
        return self.Solve()

        