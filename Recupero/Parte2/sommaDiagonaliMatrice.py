def sum_primary_diagonal(matrix:list[list[int]]) -> int:

    result = 0


    for i in range(len(matrix)):

        result += matrix[i][i]
    
    return result

def sum_secondary_diagonal(matrix:list[list[int]]) -> int:

    result = 0
    len_matrix = len(matrix)


    for i in range(len_matrix):

        result += matrix[i][len_matrix - 1 - i] # mi permette di prendere indici 2,1,0 da ogni lista
    
    return result


mat1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
print("Somma diagonale primaria: ", sum_primary_diagonal(mat1))
print("Somma diagonale secondaria: ", sum_secondary_diagonal(mat1))

