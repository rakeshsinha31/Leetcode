def removeElement(nums: list, val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            print(nums)
            k += 1
    return k

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))

# i =2, k =1