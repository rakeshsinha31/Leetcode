# Two Sum

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15,18,20,25], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Iterative
def iterative_two_sum(arr, target):
	for i,j in enumerate(arr):
		for k,l in enumerate(arr):
			if j + l == target:
				return [i, k]

# Using binary search - discard all the elements which are greater than target
# Assuming no negative numbers are in the list
def two_sum(arr, target):
	mid = len(arr)/2
	arr = sorted(arr)
	if arr[mid] >= target:
		arr = arr[0:mid]
		return arr

# Linear
def linear_two_sum(arr, target):
	d = {}
	for i,j in enumerate(arr):
		if j not in d:
			d[target-j] = i
		else:
			return [d[j], i]

#print iterative_two_sum([2, 7, 11, 15,18,20,25], 9)
#print two_sum([2, 7, 11, 15,18,20,25], 9)
print linear_two_sum([2, 7, 11, 15,18,20,25], 25)