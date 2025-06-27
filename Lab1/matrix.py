class matrix:
    def __init__(self, arg, const=0):
        if(isinstance(arg, tuple)):
            self.__matrix = []
            if(not isinstance(arg[0], int) or not isinstance(arg[0], int)):
                raise ValueError("Niepoprawny rozmiar macierzy")
            elif(arg[0] < 1 or arg[1] < 1):
                raise ValueError("Niepoprawny rozmiar macierzy")
            else:
                for i in range(arg[0]):
                    row_list = []
                    for j in range(arg[1]):
                        row_list.append(const)
                    self.__matrix.append(row_list)
        elif(isinstance(arg, list)):
            self.__matrix = []
            for row in arg:
                if (not isinstance(row, list)):
                    raise ValueError("Należy podać listę list")
                else:
                    row_list = []
                    for i in row:
                        row_list.append(i)
                    self.__matrix.append(row_list)
        else:
            raise ValueError("Niepoprawne argumenty")
        
    def size(self):
        return (len(self.__matrix), len(self.__matrix[0]))
    
    def __str__(self):
        to_print = ""
        for row in self.__matrix:
            to_print += "|"
            for val in row:
                to_print += f" {val}"
            to_print += " |\n"
        return to_print
        
    def __getitem__(self, i):
        if(not isinstance(i, int)):
            raise ValueError("Należy podać liczbę całkowitą")
        return self.__matrix[i]
    
    def __add__(self, add_matrix):
        if(add_matrix.size() != self.size()):
            raise ValueError("Niezgodne wymiary macierzy")
        tmp_matrix = matrix(self.size())
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                tmp_matrix[i][j] = add_matrix[i][j] + self[i][j]
        return(tmp_matrix)

    def __mul__(self, mul_matrix):
        if (self.size()[1] != mul_matrix.size()[0]):
            raise ValueError("Niezgodne wymiary macierzy")
        tmp_matrix = matrix((self.size()[0], mul_matrix.size()[1]))
        for i in range(self.size()[0]):
            for j in range(mul_matrix.size()[1]):
                for k in range(self.size()[1]) :
                    tmp_matrix[i][j] += self[i][k] * mul_matrix[k][j]
        return tmp_matrix
    
def matrix_transpose(t_matrix:matrix):
    if(not isinstance(t_matrix, matrix)):
        raise ValueError("Należy podać macierz")
    tmp_matrix = matrix((t_matrix.size()[1], t_matrix.size()[0]))
    for i in range(t_matrix.size()[0]):
        for j in range(t_matrix.size()[1]):
            tmp_matrix[j][i] = t_matrix[i][j]
    return tmp_matrix

def main():
    a = matrix([[1, 0, 2], [-1, 3, 1]])
    b = matrix((2, 3), 1)
    c = matrix([[3, 1], [2, 1], [1, 0]])

    print(matrix_transpose(a))
    print(a+b)
    print(a*c)
if __name__ == '__main__':
    main()