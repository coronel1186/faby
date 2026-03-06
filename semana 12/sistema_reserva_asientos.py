# Sistema de Reserva de Asientos

asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir al usuario la fila y columna del asiento a reservar
print("=== SISTEMA DE RESERVA DE ASIENTOS ===\n")
print("Las filas van de 1 a 3")
print("Las columnas van de 1 a 4\n")

fila = int(input("Ingrese la fila del asiento a reservar (1-3): ")) - 1
columna = int(input("Ingrese la columna del asiento a reservar (1-4): ")) - 1

# Validación
if 0 <= fila < 3 and 0 <= columna < 4:
    if asientos[fila][columna] == 0:
        # Marcar el asiento como reservado
        asientos[fila][columna] = 1
        print(f"\n✓ Asiento fila {fila + 1}, columna {columna + 1} reservado exitosamente.\n")
    else:
        print(f"\n✗ El asiento fila {fila + 1}, columna {columna + 1} ya está reservado.\n")
else:
    print("\n✗ Posición inválida. Ingrese valores dentro del rango.\n")

# Mostrar la matriz completa en formato tabla usando bucles anidados
print("=== ESTADO DE ASIENTOS ===")
print("(0 = Disponible, 1 = Reservado)\n")

# Encabezado de columnas
print("    Columna:", end=" ")
for col in range(4):
    print(f"{col + 1}  ", end="")
print("\n")

# Mostrar filas
for fila in range(3):
    print(f"Fila {fila + 1}:    ", end="")
    for columna in range(4):
        print(f"{asientos[fila][columna]}  ", end="")
    print()