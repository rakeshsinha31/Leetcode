def sum_of_sub_array(arr: list, length: int) -> int:
    # i,j = 0,1
    # sum = 0
    # ll = []
    # for i in range(len(l)-2):
    # # while i <= len(arr):
    #     sum = l[i] + l[i+1] + l[i+2]
    #     ll.append(sum)
    #     # i += 1
    # return max(ll)

    # Second Approach
    i = 0
    j = 0
    arr1 = []
    sum = 0
    # j = length
    while j <= len(arr) -1 :
        if j-i+1 < length:
            j += 1
            sum = sum+arr[j]
        elif j-i+1 == length:
            arr1.append(sum)
            # sum = 0
            i += 1
            j += 1
    print(arr1)








l = [2,5,3,7,8,1,8,6]
ll = sum_of_sub_array(l, 3)
print(ll)