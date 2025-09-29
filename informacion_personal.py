# 1) Crear el diccionario con las claves requeridas.

informacion_personal = {
    "nombre": "Christian Rodriguez",
    "edad": 18,
    "ciudad": "Santa Elena",
   }

# Mostrar el diccionario inicial
print("Diccionario inicial:")
print(informacion_personal)
print()

# 2) Acceder y modificar el valor asociado a "ciudad"
#    Primero mostramos la ciudad actual, luego la cambiamos.
print("Ciudad actual:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"  # la cambiamos a otra ciudad
print("Ciudad modificada a:", informacion_personal["ciudad"])
print()


# 3) Verificar existencia de la clave "telefono" y agregarla si falta
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593987654321"  # número ficticio
    print("Se agregó 'telefono':", informacion_personal["telefono"])
else:
    print("'telefono' ya existe:", informacion_personal["telefono"])
print()

# 5) Eliminar la clave "edad"
if "edad" in informacion_personal:
    informacion_personal.pop("edad")
    print("Se eliminó la clave 'edad'.")
else:
    print("La clave 'edad' no existía.")
print()

# 6) Imprimir el diccionario final con todas las modificaciones
print("Diccionario final:")
print(informacion_personal)
