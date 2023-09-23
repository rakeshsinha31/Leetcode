def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j - 1] > nums[j] and j > 0:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


arr = [5, 3, 2, 5, 12, 17, 4]
print(insertion_sort(arr))
