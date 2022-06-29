import math
import numpy as np


def true_round(num):
    ceiling = math.ceil(num)
    floor = math.floor(num)
    if math.fabs(num - ceiling) <= math.fabs(num - floor):
        return ceiling
    return floor

def true_round_matrix(num):
    ceiling = np.ceil(num)
    floor = np.floor(num)
    mask = np.fabs(num - ceiling) <= np.fabs(num - floor)
    result = np.zeros_like(num)
    result[np.where(mask == True)] = ceiling[np.where(mask == True)]
    result[np.where(mask == False)] = floor[np.where(mask == False)]
    return result
