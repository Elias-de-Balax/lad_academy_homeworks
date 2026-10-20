"""Звёздочка (вложенные списки / матрица). Создайте матрицу 3×4 — список из трёх строк по четыре числа. Выведите:
   а) сумму всех элементов; б) сумму элементов в каждой строке; в) максимальный элемент во всей матрице;
   г) «транспонированную» матрицу (строки и столбцы поменять местами) — разберитесь самостоятельно, как это сделать
   через вложенные циклы и comprehension."""

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

sum_rows = [sum(row) for row in matrix]

print("Сумма элементов в каждой строке:", sum_rows)
print("Сумма всех элементов матрицы:", sum(sum_rows))
print("Максимальный элемент во всей матрице:", max(max(row) for row in matrix))

rows = len(matrix)
cols = len(matrix[0])

# Создаем пустую матрицу размером cols x rows
transposed_matrix = [[0] * rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transposed_matrix[j][i] = matrix[i][j]

print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)