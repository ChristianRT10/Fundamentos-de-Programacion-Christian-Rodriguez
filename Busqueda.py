# Programa 1: Búsqueda en una matriz 3x3

# Definimos la matriz
matriz = [
    [4, 7, 2],
    [9, 5, 1],
    [3, 8, 6]
]

# Función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición fila, columna
    return None

# Valor a buscar
valor_buscado = 5
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz.")
