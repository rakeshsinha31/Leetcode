def two_sum(nums: list, num) -> int:
    i=0
    j = len(nums)-1
    l = []
    nums1 = sorted(nums)
    while j>=i:
        sum = nums1[i] + nums1[j]
        if sum == num:
            l.append(nums.index(nums1[j]))
            l.append(nums.index(nums1[i]))
            break
        elif sum>num:
            j -= 1
        else:
            i+=1
    return l

nums = [5,9,3,7,16,8]
print(two_sum(nums, 16))