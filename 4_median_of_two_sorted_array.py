def findMedianSortedArrays(nums1, nums2) -> float:
    l = nums1 + nums2
    l = sorted(l)
    if len(l) % 2 == 0:
        half = int(len(l) / 2)
        median = (l[half] + l[half - 1]) / 2
    else:
        half = len(l) // 2
        median = l[half]
    return median


findMedianSortedArrays([1, 2], [3, 4])
