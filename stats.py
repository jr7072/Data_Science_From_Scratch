'''
    Author: Juan Rosales
    Date: 2023-03-20
    
    All code in this file is referenced from the book
    data science from scratch (2nd Edition) by Joel Grus
'''
import math
from collections import Counter, defaultdict

from typing import List

'''
    Central Tendencies
'''

# mean of observations
def mean(xs: List[float]) -> float:
    '''
        calculates the mean of a list of observations

        xs (List[float]): list of observations

        returns (float): mean of the observations
    '''

    return sum(xs) / len(xs)

assert mean([2, 3, 4]) == 3


# median
def median(xs: List[float]) -> float:
    '''
        returns the median of a list of observations

        xs (List[float]): list of observations

        returns (float): median of xs 
    '''

    assert xs, 'expected xs to have at least 1 observation'

    # sort xs
    sorted_xs = sorted(xs)

    xs_len = len(sorted_xs)
    median_index = xs_len // 2

    if xs_len % 2 == 0:
        
        right_index = median_index
        median_index -= 1 # subtract 1 since len(xs) / 2 chooses middle right index
        mid_sum = sorted_xs[median_index] + sorted_xs[right_index]

        return mid_sum / 2
    
    return sorted_xs[median_index]

assert median([1, 2, 3]) == 2
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 2, 3, 4, 5, 6]) == 3.5
assert median([4, 1, 2]) == 2


# quantile
def quantile(xs: List[float], quantile: float) -> float:
    '''
        gets the nth quantile from a list of observations

        xs (List[float]): list of observation

        quantile (float): The nth percent desired from the observations

        returns (float): The value located at the index that is the quantile
    '''

    assert xs, "expected xs to have at least one observation"
    assert quantile >= 0 and quantile <= 1, \
         'expected quantile to be in range 0 to 1 (inclusive)'

    sorted_xs = sorted(xs)
    largest_idx = len(xs) - 1
    nth_idx = math.floor(largest_idx * quantile)

    return sorted_xs[nth_idx]

assert quantile([1, 2, 3], .5) == 2
assert quantile([1, 2, 3, 4], .75) == 3
assert quantile([1, 2, 5, 6, 6, 6], .25) == 2


# mode
def mode(xs: List[float]) -> List[float]:
    '''
        returns the modes from a list of observations

        xs (List[float]): Float list of observations

        returns (List[float]): The most freq values in xs
    '''

    value_counts = Counter(xs)
    max_count = max(value_counts.values())
    inverse_map = defaultdict(list)
    
    for value, count in value_counts.items():
        inverse_map[count].append(value)

    return inverse_map[max_count]

assert mode([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert mode([1, 3, 4, 4, 4]) == [4]


'''
    dispersion section
'''