# Registro de Temperaturas Diarias

# Ciudades que vamos a usar
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D de temperaturas
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

# FUNCIÓN PARA CALCULAR TEMPERATURAS PROMEDIO

def calcular_promedios(ciudades, temperaturas):
    resultados = {}

    for i in range(len(ciudades)):  # Recorremos las ciudades
        ciudad = ciudades[i]
        resultados[ciudad] = []  # Guardamos los promedios de cada semana

        for j in range(len(temperaturas[i])):  # Recorremos las semanas
            suma = sum(temperaturas[i][j])  # Sumamos los días de la semana
            promedio = suma / len(temperaturas[i][j])  # Calculamos promedio
            resultados[ciudad].append(round(promedio, 2))  # Guardamos con 2 decimales

    return resultados

# PRUEBA DE LA FUNCIÓN
promedios = calcular_promedios(ciudades, temperaturas)

# Mostramos los resultados de manera ordenada
for ciudad, lista_promedios in promedios.items():
    print("Ciudad:", ciudad)
    for semana, promedio in enumerate(lista_promedios, start=1):
        print(f"  Semana {semana} → Promedio de temperatura: {promedio} °C")
    print()

