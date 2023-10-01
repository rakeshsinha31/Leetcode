# First Negative Number in every Window of Size K | Sliding Window


def find_negative(nums, size):
    l, r = 0, 0
    res = []
    aux_list = []
    while l <= len(nums) - 1:
        if (r - l + 1) < size:
            r += 1
        elif (r - l + 1) >= size:
            if nums[r] < 0:
                if len(aux_list) ==0:
                    
                res.append(nums[r])
                r += 1
                l + 1
    return res


size = 3
nums = [12, -1, -7, 8, -15, 30, 16, 28]
print(find_negative(nums, size))
