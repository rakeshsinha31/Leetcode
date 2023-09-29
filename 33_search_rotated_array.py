# 33. Search in Rotated Sorted Array
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] < nums[mid]:
            if target < nums[mid] and target < nums[l]:






nums = [4, 5, 6, 7, 0, 1, 2]
target = 7
search(nums, target)
