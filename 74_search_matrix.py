# 74. Search a 2D Matrix


def search_matrix(matrix, target):
    new_mat = []
    matrix = [new_mat.extend(i) for i in matrix]
    l, r = 0, len(new_mat) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == new_mat[mid]:
            return True
        if target > new_mat[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 620
print(search_matrix(matrix, target))
