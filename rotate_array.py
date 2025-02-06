def rotate(nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k%len(nums)
    def reverse(nums, l, r):
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    nums = reverse(nums, l=0, r = len(nums)-1)
    nums = reverse(nums, l=0, r = k-1)
    nums = reverse(nums, l=k, r = len(nums)-1)
    return nums

    




nums = [-1]
k = 2
ll = rotate(nums, k)
print(ll)