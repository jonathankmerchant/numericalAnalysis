'''Author: Jon
   Date: 03/10/22
   Description: Newton-Raphson Root Finding Algorithm
   Complexity:
            -Best case: O(1)
            -Worst case: O(n)
   Arguments: 
            -initGuess: Initial guess for location of root (double)
            -tol: Stop algorithm if within tol tolerance
            -maxCount: Stop algorithm if exceeding maxCount iterations
   Returns:
            -Double value estimating root (if converges; possibly does not)
            -Null if calculation does not converge
   Other Utilized Functions:
            -initFunc: Function whose roots we wish to find
            -derivFunc: Derivative of above function
'''
import numpy as np


iterCount = 0

def newtonRaphson(initGuess, tol, maxCount):
  
  x = double(initGuess)    #Forces double if not already
  
  while(iterCount <= maxCount):
    f = initFunc(x)       #Evaluating function at x
    f_prime = derivFunc(x)    #Evaluating derivative at x
    
    x_next = x - f/f_prime  #Actual calculation
    
    if (np.abs(x_next - x) < tol):
      return x
    else:
      x = x_next    #If not within tol, repeat calculation
    
  return null
