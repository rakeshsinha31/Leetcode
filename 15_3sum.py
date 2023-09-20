def twoSum(nums):
    nums.sort()
    res = []
    for i, j in enumerate(nums):
        if i > 0 and j == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = j + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([j, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        print(res)
        return res


n = [-4, -1, -1, 0, 1, 2]
twoSum(n)
