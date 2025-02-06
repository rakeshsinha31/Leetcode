def search_rotated_arr(nums: list, target:int) -> int:

    for i in range(len(nums)-1):
        # if nums[i] < nums[i+1]:
            # pivot_idx = i
        if nums[i] == target:
            return i
    return -1






l = [4,5,6,7,0,1,2]
t = 0
print(search_rotated_arr(l, t))