# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primera compra: solo monto (usa 10% por defecto)
monto1 = float(input("Ingrese el monto de la primera compra: "))
descuento1 = calcular_descuento(monto1)
total1 = monto1 - descuento1

print("\nCompra 1:")
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${total1}")

# Segunda compra: monto + porcentaje
monto2 = float(input("Ingrese el monto de la segunda compra: "))
porcentaje2 = float(input("Ingrese el porcentaje de descuento: "))
descuento2 = calcular_descuento(monto2, porcentaje2)
total2 = monto2 - descuento2

print("Compra 2:")
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${total2}")
