def sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) ==0:
        return []
    mid = len(arr)//2
    pivot = arr[mid]
    smaller, equal, larger = [],[],[]
    for j,i in enumerate(arr):
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)
    return sort(smaller) + equal + sort(larger)


def findMedianSortedArrays(nums1, nums2):
    req_list = sort( nums1+nums2)
    print req_list
    if len(req_list) %2 == 0:
        return float(req_list[len(req_list)//2] + req_list[(len(req_list)//2)-1])/2
    else:
        return float(req_list[len(req_list)//2])/2

print findMedianSortedArrays([1,3],[2])