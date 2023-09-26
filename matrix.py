class Matrix:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def insert_data(self):
        mat = []
        for i in range(self.row):
            l = []
            for j in range(self.col):
                val = input("Enter value {}x{}: ".format(i, j))
                l.append(int(val))
            mat.append(l)
        return mat

    def addition(self, mat1, mat2):
        result_mat = []
        for i in range(len(mat1)):
            l = []
            for j in range(len(mat1[0])):
                # result_mat[i][j] = mat1[i][j] + mat2[i][j]
                l.append(mat1[i][j] + mat2[i][j])
            result_mat.append(l)
        return result_mat

    def multiplication(self, mat1, mat2):
        result_mat = [[0] * len(mat1)] * len(mat2[0])
        # print(result_mat)
        # result_mat = []
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    result_mat[i][j] += mat1[i][k] + mat2[k][j]
            # result_mat.append(l)
        print(result_mat)


m = Matrix(2, 2)
m1 = m.insert_data()
m2 = m.insert_data()
print(m1)
print(m2)
# add = m.addition(m1, m2)
# print(add)
mul = m.multiplication(m1, m2)
print(mul)
