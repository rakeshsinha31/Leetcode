def average_of_subarray(arr, length):
    avg = []
    for i in range(len(arr)):
        sub_arr = arr[i : length + i]
        if len(sub_arr) != 5:
            break
        avg.append(sum(sub_arr) / 5)
    print(avg)


l = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5
average_of_subarray(l, K)
