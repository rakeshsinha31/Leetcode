def selection_sort(arr):
    """
    Selection Sort: loop the given array and find the index of the minimum value in it.
    Once get the min value swap it with left of item of the unsorted sub array
    """

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = [5, 0, 3, 5, 12, 17, 4]
print(selection_sort(arr), "<----f")
