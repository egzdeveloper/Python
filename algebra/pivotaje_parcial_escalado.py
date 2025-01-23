from typing import Any
import numpy as np


def pivotaje_parcial_escalado(matrix):
    # Convierte la matriz a un array propio de numpy y establece los elementos a tipos flotantes
    matrix = np.array(matrix, dtype=float)

    # Obtenemos el número de filas de la matriz
    n = len(matrix)

    # Se imprime la matriz
    print("\nMatriz original:")
    print(matrix)

    print('\n------------------ RESOLUCIÓN ---------------------------')

    for i in range(n - 1):
        print(f"\nPASO {i + 1}:\n")

        # Encuentra el índice del máximo valor en la columna actual
        max_index = np.argmax(np.abs(matrix[i:, i])) + i

        # Intercambia las filas si es necesario
        if max_index != i:

            # Realiza el intercambio entre filas donde se busca colocar el máximo valor en la posición (1,1)
            matrix[[i, max_index], :] = matrix[[max_index, i], :]

            # Se imprime y se redondea a dos decimales
            print("Matriz después del intercambio:")
            print(np.round(matrix, 2), '\n')

        # Consigue ceros por debajo del elemento diagonal
        for j in range(i + 1, n):

            # Se calcula el factor de multiplicación, es decir, el valor con el que es necesario multiplicar
            # la fila para obtener un cero debajo de la diagonal de la matriz
            factor: Any = matrix[j, i] / matrix[i, i]
            print(f"-> Factor de multiplicación para la fila {j + 1}: {round(factor, 2)}")

            # Realiza la operación de actualización donde se multiplica la fila por el factor obtenido antes
            matrix[j, i:] -= factor * matrix[i, i:]

        # Imprime la matriz después de hacer ceros por debajo del elemento diagonal
        print("\nMatriz después de hacer ceros:")
        print(np.round(matrix, 2))

    return matrix


# Ejemplo de uso
matriz_1 = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3],
    [4, -2, 3, 9]
]

matriz_triangular_superior_1 = pivotaje_parcial_escalado(matriz_1)

# Imprime la matriz triangular superior resultante
print('\n\n------------------ SOLUCIÓN ---------------------------')
print("\nMatriz triangular superior resultante:")
print(np.round(matriz_triangular_superior_1, 2), "\n")