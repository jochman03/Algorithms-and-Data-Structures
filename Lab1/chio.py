class matrix:
    __matrix = []
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
    def __setitem__(self, i, val):  
        self.__matrix[i] = val
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


def chio_det(A_matrix:matrix):
    if (not isinstance(A_matrix, matrix)):
        raise ValueError("Należy podać macierz")
    if (A_matrix.size()[0] != A_matrix.size()[1]):
        raise ValueError("Macierz musi być kwadratowa")
    n = A_matrix.size()[0]
    if (n < 2):
        raise ValueError("Metoda tylko dla n > 2")
    if (n == 2):
        return A_matrix[0][0] * A_matrix[1][1] - A_matrix[0][1] * A_matrix[1][0]
    c = 1
    if (A_matrix[0][0] == 0):
        for i in range(1, n):
            if(A_matrix[i][0] != 0):
                A_matrix[0], A_matrix[i] = A_matrix[i], A_matrix[0]
                c = -c
                break
    c = c/pow(A_matrix[0][0], n-2)
    tmp_matrix = matrix((n-1, n-1))
    for i in range(n-1):
        for j in range(n-1):
            tmp_matrix[i][j] = A_matrix[0][0] * A_matrix[i+1][j+1] - A_matrix[i+1][0] * A_matrix[0][j+1]
    return c * chio_det(tmp_matrix)

def main():
    a = matrix([

    [5 , 1 , 1 , 2 , 3],

    [4 , 2 , 1 , 7 , 3],

    [2 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]

    ])
    b = matrix(  [
        [0 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
        ])

    print(chio_det(a))
    print(chio_det(b))

if __name__ == '__main__':
    main()