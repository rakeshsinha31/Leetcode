
def merge(nums1: list, m, nums2: list, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1
    k = m+n -1

    while i>=0 and j>=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-= 1
        else:
            nums1[k] = nums2[j]
            j-= 1
        k-=1
    if j>=0:
        nums1[k] = nums2[j]
        j-=1
        k-=1

    
        



l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
ll = merge(l1, l2)
print(ll)