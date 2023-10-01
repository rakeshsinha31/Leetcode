# find the max sum of a subarray of length 2
def max_sum_of_subarray(nums, size):
    s = []
    l, r = 0, 0
    for i in range(len(nums) - 2):
        cur_sum = nums[i] + nums[i + 1] + nums[i + 2]
        print(cur_sum)
        s.append(cur_sum)
    return max(s)


nums = [4, 25, 6, 7, 0, 1, 21]
size = 2

print(max_sum_of_subarray(nums, size))
