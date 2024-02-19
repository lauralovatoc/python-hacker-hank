def add(matrix1, matrix2):
    #return [[i1 + i2 for i1, i2 in zip(list1, list2)] for list1, list2 in zip(matrix1, matrix2)]

    return[[sum(elements) for elements in zip (list1, list2)] for list1, list2 in zip(matrix1,matrix2)]

    #i1 i2 vao ser somados a cada for que vair percorrer i1 e i2 dentro das listas 1 e 2 (matrix1 e matrix2)
    #depois um laço d repetição vai percorrer as somas dentro das listas 1 e 2 que foram concatenadas com a funcção zip (juntando matrix 1 e matrix2)

if '__name__' == '__main__':
    m1 = [[1, -2], [-3, 4]]
    m2 = [[2, -1], [0, -1]]

    result = add(m1, m2)
    print(result)
