# Registro de Temperaturas Diarias

# Ciudades que vamos a usar
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Vamos a suponer que tenemos 2 semanas de datos
# Matriz 3D de temperaturas (números inventados)
temperaturas = [
    [   # Quito
        [18, 19, 20, 21, 20, 19, 18],   # Semana 1
        [19, 20, 21, 22, 21, 20, 19]    # Semana 2
    ],
    [   # Guayaquil
        [28, 29, 30, 31, 30, 29, 28],   # Semana 1
        [29, 30, 31, 32, 31, 30, 29]    # Semana 2
    ],
    [   # Cuenca
        [15, 16, 17, 16, 15, 14, 15],   # Semana 1
        [16, 17, 18, 17, 16, 15, 16]    # Semana 2
    ]
]

# Ahora calculamos el promedio de cada ciudad en cada semana
for i in range(len(ciudades)):  # Recorremos las ciudades
    print("Ciudad:", ciudades[i])
    for j in range(len(temperaturas[i])):  # Recorremos las semanas
        suma = 0
        for k in range(len(temperaturas[i][j])):  # Recorremos los días
            suma += temperaturas[i][j][k]
        promedio = suma / len(temperaturas[i][j])
        print("  Semana", j+1, "→ Promedio de temperatura:", promedio, "°C")
    print()  # Espacio entre ciudades
