def quicksort_inplace(arr, low=0, high=None):
    if high == None:
        high = len(arr) - 1
    # print(low, high)
    if low < high:
        partition_idx = partition(arr, low, high)
        print(partition_idx)
        quicksort_inplace(arr, low, partition_idx - 1)
        quicksort_inplace(arr, partition_idx + 1, high)
    return arr


def partition(arr, low, high):
    i = low
    pivot = arr[high]
    j = high - 1

    while i < j:
        while arr[i] < pivot and i < high:
            i += 1
        while arr[j] >= pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i


arr = [22, 11, 88, 66, 55, 77, 44, 44]
# print(quicksort_inplace(arr))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    smaller = []
    greater = []
    equal = []
    pivot = arr[len(arr) - 1]
    for i in arr:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            smaller.append(i)
        else:
            equal.append(i)
    return quick_sort(smaller) + equal + quick_sort(greater)


arr = [22, 11, 88, 66, 55, 77, 44, 44]
print(quick_sort(arr))
