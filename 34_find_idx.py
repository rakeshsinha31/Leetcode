# 34. Find First and Last Position of Element in Sorted Array


def find_idx(nums, target):
    l, r = 0, len(nums) - 1
    req_idx = []
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            req_idx.append(mid)
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return req_idx


nums = [11, 11, 22, 22, 44, 55, 66, 77, 88]
target = 22
print(find_idx(nums, target))
