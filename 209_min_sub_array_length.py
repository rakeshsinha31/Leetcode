# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


def min_subarray_len(nums, target):
    sums = []
    l, r = 0, 0
    res = []
    cur_sum = 0
    while l <= r:
        if cur_sum < target:
            r += 1
            cur_sum += nums[r]
        elif cur_sum >= target:
            l += 1

    return res


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(min_subarray_len(nums, target))
