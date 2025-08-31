# Programa 2: Ordenación de una fila en una matriz 3x3

# Definimos la matriz
matriz = [
    [4, 7, 2],
    [9, 5, 1],
    [3, 8, 6]
]

# Función Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegimos la fila a ordenar (ejemplo: fila 1 -> segunda fila)
indice_fila = 1
bubble_sort(matriz[indice_fila])

# Mostrar matriz modificada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
