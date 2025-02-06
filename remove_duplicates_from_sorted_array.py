def remove_duplicates(nums: list) -> int:
    l=1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    print(nums)
    return l



        


l = [0,0,1,1,1,2,2,3,3,4]
ll = remove_duplicates(l)
print(ll)