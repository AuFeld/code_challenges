### Description ###

'''
Given an array of integers, return indices of the two numbers such that they 
add up to specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

### Approach ###

'''
To take advantage the dictionary and the notes that there is one and only one 
solution. To search the target-num in the saved lookup dictionary when saving 
the num in the lookup dictionary one by one. This method could save the space 
and also prevent the index overwriting when there are two same values in the 
nums. 
'''

### Code ###

def twosum(self, nums, target):
    lookup = {}
    for count, num in enumerate(nums):
        if target - num in lookup:
            return lookup[target-num], count
        lookup[num] = count   