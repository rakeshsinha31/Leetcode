# 35. Search Insert Position


def search_insert(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            print("equal-->", mid)
            return mid
        if target > nums[mid]:
            print("if-->", mid)
            l = mid + 1
        else:
            print("else-->", mid)
            r = mid - 1
    return l


nums = [7, 8, 10, 14, 16, 21]
target = 0
print(search_insert(nums, target))
