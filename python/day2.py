"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


==== 
Solution : 
we multiply all the elements of the array then we devide by each element of create the new array 

"""

from functools import reduce


def get_multiples_array(tab):
    mul = reduce(lambda x, y: x*y, tab)
    return map(lambda x: mul/x, tab)

## naive 
def get_multiples_array_v2(tab):
    result = []
    for i in range(0, len(tab)):
        tmp = 1
        for j in range(0, len(tab)):
            if i != j:
                tmp *= tab[j]
        result.append(tmp)
    return result

## optimized 

test = [1, 2, 3, 4, 5]
print(get_multiples_array_v2(test))
