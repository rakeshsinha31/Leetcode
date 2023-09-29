# 162. Find Peak Element
def find_peak(nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if mid > 0 and mid < r:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        elif mid == 0:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        elif mid == len(nums) - 1:
            if nums[len(nums) - 1] > nums[len(nums) - 2]:
                return len(nums) - 1
            else:
                return len(nums) - 2


nums = [16, 5, 3, 2, 1]
print(find_peak(nums))
