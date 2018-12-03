'''
Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''


l = [1, 20, 3]


def get_max(arr):
    odd = 0
    even = 0
    for i in range(0, len(arr), 2):
        if arr[i] > 0:
            even += arr[i]
        if i+1 < len(arr) and arr[i+1] > 0:
            odd += arr[i+1]
    if odd > even:
        return odd
    return even


print(get_max(l))
