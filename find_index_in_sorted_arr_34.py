def searchRange(nums: list, target: int) -> list:
    l=0
    r=len(nums)-1
    
    # for i in range(len(nums)):
    while r >= l:
        mid = (l+r)// 2
        if target == nums[mid]:
            if nums[mid] == nums[mid-1]:
                return [mid-1, mid]
            if nums[mid] == nums[mid+1]:
                return [mid, mid+1]
        elif target > nums[mid]:
            l = mid+1
        else:
            r = mid-1

    return [-1, -1]

nums = [7,7]
target = 7
print(searchRange(nums, target))