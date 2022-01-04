import sigfig
from sympy import *
import time

class bracketingMethodSolver:
    '''
    params: lower bound / upper bound / tolerance(Es) / function / number of significant figures / no. of iterations
    returns: lower bound list / upper bound list / number of iterations / root(xr) / function used / time
    '''
    def bisect(self,lower,upper,tol,functionString,n, max_iterations):
        start = time.perf_counter()
        x = Symbol('x')
        f = functionString
        f = lambdify(x, f)
        if f(lower)*f(upper) > 0:
            return "the two roots are either positive or negative"
        elif(f(lower) == 0):
            return f'the root is {lower}'
        elif(f(upper) == 0):
            return f'the root is {upper}'
        xr = 0
        i = 0
        upper_List = []
        lower_List = []
        upper_List.append(upper)
        lower_List.append(lower)
        while(i < max_iterations):
            xrnew = sigfig.round(sigfig.round((upper+lower),sigfigs = n)/2.0,sigfigs = n)
            i += 1
            # print(f'lower limit : {lower} | upper limit : {upper} | root: {xrnew} | f(lower) = {f(lower)} | f(upper) = {f(upper)} | f(xr) = {f(xrnew)} | error = {abs(xrnew-xr)}')
            if(abs(xr-xrnew) < tol):
                xr = xrnew
                break
            value = f(lower)*f(xrnew)
            xr = xrnew
            if(value < 0):
                upper = xrnew
            elif(value > 0):
                lower =xrnew
            else:
                break
            upper_List.append(upper)
            lower_List.append(lower)
        # print(f'xr = {xr} and no. of iterations = {i}')
        if(i == max_iterations):
            return "maximum iterations reached"
        end = time.perf_counter()
        return [lower_List,upper_List,i,xr,f,end - start]
    '''
    params: lower bound / upper bound / tolerance(Es) / function / number of significant figures / no. of iterations
    returns: lower bound list / upper bound list / number of iterations / root(xr) / function used / time
    '''
    def regula(self,a,b,tol,functionString,n, max_iterations):
        start = time.perf_counter()
        x = Symbol('x')
        f = functionString
        f = lambdify(x, f)
        upper=0.0
        lower=0.0
        MR1=0.0
        MR2=0.0
        upper_List = []
        lower_List = []
        itr = 1
        if f(a)*f(b) > 0:
            return "the two roots are either positive or negative"
        elif(f(a) == 0):
            return f'the root is {a}'
        elif(f(b) == 0):
            return f'the root is {b}'
        if f(a)>0:
            upper=a
            lower=b
        else:
            upper=b
            lower=a
        upper_List.append(upper)
        lower_List.append(lower)
        MR1=((lower*f(upper))-(f(lower)*upper))/(f(upper)-f(lower))
        MR1 = sigfig.round(MR1, sigfigs = n)
        FMR1 = f(MR1)
        FMR1 = sigfig.round(FMR1, sigfigs = n)
        if f(lower)*FMR1 < 0:
            upper=MR1
        elif f(upper)*FMR1 < 0:
            lower=MR1
        elif(FMR1 == 0) :
            end = time.perf_counter()
            return [lower_List,upper_List,itr,MR1,f, end - start]
        while(True):
            itr=itr+1
            MR2=((lower*f(upper))-(f(lower)*upper))/(f(upper)-f(lower))
            MR2 = sigfig.round(MR2, sigfigs = n)
            FMR2 = f(MR2)
            FMR2 = sigfig.round(FMR2, sigfigs = n)
            if f(lower)*FMR2 < 0:
                upper=MR2
            elif f(upper)*FMR2 < 0:
                lower=MR2
            upper_List.append(upper)
            lower_List.append(lower)
            if(abs(MR2-MR1)<tol or itr >= max_iterations):
                end = time.perf_counter()
                if(itr == max_iterations):
                    return "maximum iterations reached"
                return [lower_List,upper_List,itr,MR2,f, end - start]
            else:
                MR1=MR2

