# CMT309 Coursework 2
# student number: C1937886

import numpy as np
def broadcast(fun, a, b):
    """
    broadcast function takes two input arrays and performs element-wise
    mathematical operations. If the arrays have different sizes, including
    different dimensions, the function matches them and the output array has 
    the maximum shape.
    
    :param fun: the mathematical operation that needs to be executed
    :param a: first input array
    :param b: second input array
    
    :return: returns an output array which is the product of the executed
    mathematical function between array a and b.
    """
 # create a new array of ones to fit in the two input array shapes. 
 # the new array has number of collumns equal to the number of
 # dimensions of the higher dimensional array from the two input arrays.
    new_ar = np.full((2, max(a.ndim, b.ndim)), fill_value = 1, dtype = int)  
  
 # fitting the input arrays shapes into the new array. Shape of array a
 # is placed at the end of first row  and shape of the array b is placed
 # at the end of second.
    
    for i in new_ar:
        new_ar[0,-a.ndim:] = np.shape(a)
  
    for i in new_ar:
        new_ar[1,-b.ndim:] = np.shape(b)
    
 # finding the desired shape by determining
 # the maximum value of each collumn from the new array 
 # which includes the two input array shapes.

    desired_shape = np.max(new_ar, axis = 0)

 # finding how much each of the input arrays should be extended in order
 # to be broadcasted
    fit_ar1 = np.floor_divide(desired_shape, new_ar[0])
    fit_ar2 = np.floor_divide(desired_shape, new_ar[1])
    
 # extending each of the input arrays individually to the desired shape 
 # and storing the function to be executed between the two maximum shaped arrays.
    try:
        final_array1 = np.tile(a, fit_ar1)
        final_array2 = np.tile(b, fit_ar2) 
        result = fun(final_array1, final_array2)
        
 # render brodcasting unavailable if any of the of the dimensions  of one 
 # array is not multiple of the equivalent dimension of the other.
    except: 
        if (new_ar[0] / new_ar[1]).any():
            print('Cannot Broadcast')
            return None
    return result
    
