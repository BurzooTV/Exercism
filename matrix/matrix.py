class Matrix:
    def __init__(self, matrix_string):
        self.__split_list = matrix_string.split('\n')
        self.matrix = [[int(number) for number in matrix.split(' ')]for matrix in self.__split_list]


    def row(self, index):
        return self.matrix[index - 1]


    def column(self, index):
        return [col[index - 1] for col in self.matrix]
