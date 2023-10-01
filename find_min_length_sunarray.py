# find the min length of a sunarray which sums to target
def min_len_subarray(nums, target):
    l, total = 0, 0
    res = len(nums)
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1
    return res


nums = [4, 1, 3, 2, 6, 7]
target = 6
print(min_len_subarray(nums, target))
