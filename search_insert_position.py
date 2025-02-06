def search_insert_position(nums, target):
    l = 0
    r = len(nums)-1
    # mid =-1

    while r >= l:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid+1
        else:
            r = mid-1
    if mid == 0:
        if l>target:
            return 0
    return mid+1




nums = [1,3,5,6]
target = 2
print(search_insert_position(nums, target))