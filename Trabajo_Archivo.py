# 1. Escritura de Archivo de Texto
# Creamos un archivo llamado "my_notes.txt" en modo escritura ("w").
with open("my_notes.txt", "w") as file:
    file.write("Primera nota personal: Nombre: Christian Rodriguez.\n")
    file.write("Segunda nota personal: Edad: 18 Años.\n")
    file.write("Tercera nota personal: Ciudad: Salinas.\n")

# 2. Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ("r").
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea con readline()
    print("Contenido del archivo my_notes.txt:\n")
    linea = file.readline()  # Lee la primera línea
    while linea:  # Mientras exista contenido
        print(linea.strip())  # strip() quita saltos de línea extra
        linea = file.readline()  # Lee la siguiente línea
