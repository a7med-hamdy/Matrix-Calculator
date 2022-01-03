from sigfig import round
from sympy import *
import time

class bracketingMethodSolver:
    '''
    params: lower bound / upper bound / tolerance(Es) / function / number of significant figures
    returns: lower bound list / upper bound list / number of iterations / root(xr) / function used / time
    '''
    def bisect(self,a,b,tol,functionString,n):
        start = time.perf_counter()
        f = sympify(functionString)
        if f(a)*f(b) >= 0:
            return "the two roots are either positive or negative"
        xr = 0
        i = 0
        a_list = []
        b_list = []
        a_list.append(a)
        b_list.append(b)
        while(f(xr) != 0):
            xrnew = round(round((a+b),n)/2.0,n)
            i += 1
            print(f'lower limit : {a} | upper limit : {b} | root: {xrnew} | f(a) = {f(a)} | f(b) = {f(b)} | f(xr) = {f(xrnew)} | error = {abs(xrnew-xr)}')
            if(abs(xr-xrnew) < tol):
                xr = xrnew
                break
            value = f(a)*f(xrnew)
            xr = xrnew
            if(value < 0):
                b = xrnew
            elif(value > 0):
                a=xrnew
            else:
                break
            a_list.append(a)
            b_list.append(b)
        print(f'xr = {xr} and no. of iterations = {i}')
        end = time.perf_counter()
        return list(a_list,b_list,i,xr,f,end - start)
    '''
    params: lower bound / upper bound / tolerance(Es) / function / number of significant figures
    returns: lower bound list / upper bound list / number of iterations / root(xr) / function used / time
    '''
    def regula(self,a,b,tol,functionString,n):
        start = time.perf_counter()
        f = sympify(functionString)
        upper=0.0
        lower=0.0
        MR1=0.0
        MR2=0.0
        upper_List = []
        lower_List = []
        itr = 1
        if f(a)*f(b) >= 0:
            return "the two roots are either positive or negative"
        if f(a)>0:
            upper=a
            lower=b
        else:
            upper=b
            lower=a
        upper_List.append(upper)
        lower_List.append(lower)
        MR1=((lower*f(upper))-(f(lower)*upper))/(f(upper)-f(lower))
        MR1 = round(MR1, n)
        FMR1 = f(MR1)
        FMR1 = round(FMR1,n)
        if f(lower)*FMR1 < 0:
            upper=MR1
        elif f(upper)*FMR1 < 0:
            lower=MR1
        
        while(True):
            itr=itr+1
            MR2=((lower*f(upper))-(f(lower)*upper))/(f(upper)-f(lower))
            MR2 = round(MR2, n)
            FMR2 = f(MR2)
            FMR2 = round(FMR2, n)
            if f(lower)*FMR2 < 0:
                upper=MR2
            elif f(upper)*FMR2 < 0:
                lower=MR2
            upper_List.append(upper)
            lower_List.append(lower)
            if(abs(MR2-MR1)<tol):
                end = time.perf_counter()
                return list(lower_List,upper_List,itr,MR2,f, end - start)
            else:
                MR1=MR2

