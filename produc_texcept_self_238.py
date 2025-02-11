from functools import reduce
from operator import mul

def productExceptSelf(nums: list) -> list:
    ll = []
    for i in range(len(nums)):
        v = nums[i]
        nums[i] = 1
        res = reduce(mul, nums)
        ll.append(res)
        nums[i] = v
    return ll


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))