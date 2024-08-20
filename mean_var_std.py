"""
This project is part of the Data Analysis with Python Projects from FreeCodeCamp

Create a function named calculate() in mean_var_std.py that uses Numpy to output:
the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array,
and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

{
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
}

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message:
"List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.
"""
import numpy as np

def calculate(list):
    calculations = {}

    try:
        #Check list lenght
        if len(num_list) != 9:
            raise ValueError("List must contain nine numbers")
        

        #   Calculations
        matrix = np.array(num_list)
        matrix = np.reshape(matrix,(3,3))

        #       Mean
        _mean_ = [matrix.mean(axis = 1).tolist(),matrix.mean(axis = 0).tolist(),matrix.mean().tolist()]
        
        
        #   Variance
        _var_ = [matrix.var(axis = 0).tolist(),matrix.var(axis = 1).tolist(),matrix.var().tolist()]

        #   Standard Deviation  
        _std_ = [matrix.std(axis = 0).tolist(),matrix.std(axis= 1).tolist(),matrix.std().tolist()]
        
        #   Max
        max_ = [matrix.max(axis = 0).tolist(),matrix.max(axis = 1).tolist(),matrix.max().tolist()]

        #   Min
        min_ = [matrix.min(axis = 0).tolist(),matrix.min(axis = 1).tolist(),matrix.min().tolist()]

        #   Sum
        sum_ = [matrix.sum(axis=1).tolist(),matrix.sum(axis=0).tolist(),matrix.sum().tolist()]

        calculations = {
            "mean" : _mean_,
            "variance" : _var_,
            "standard deviation" : _std_,
            "max" : max_,
            "min" : min_,
            "sum" : sum_
        }

    except ValueError as ve:
        print(f"ERROR: {ve}")
        
    return calculations


