import random
# Durante este TP descubrí diferentes metodos y formas de llegar a un resultado por lo que me pareció bueno dejar comentarios para despues volver a chusmear

# Ejercicio 1
notas = [7, 8, 5, 10, 9, 6, 4, 8, 7, 9]
print("Notas de estudiantes:")
for n in notas:
    print(n)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


# Ejercicio 2
productos = []
for i in range(5):
    p = input(f"Ingrese producto {i+1}: ")
    productos.append(p)

print("Productos ordenados:")
for p in sorted(productos):
    print(p)

eliminar = input("¿Qué producto desea eliminar? ")
if eliminar in productos:
    productos.remove(eliminar)

print("Lista actualizada:")
for p in productos:
    print(p)


# Ejercicio 3
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Total pares:", len(pares))
print("Total impares:", len(impares))


# Ejercicio 4
lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for n in lista:
    if n not in sin_repetidos:
        sin_repetidos.append(n)


print("Lista sin repetidos:")
for x in sin_repetidos:
    print(x)


# Ejercicio 5
estudiantes = ["Ana", "Luis", "Marta", "Sofía", "Pedro", "Carlos", "Lucía", "Raúl"]
opcion = input("¿Desea agregar (A) o eliminar (E) un estudiante? ").upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif opcion == "E":
    borrar = input("Ingrese el nombre a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)

print("Lista final:")
for e in estudiantes:
    print(e)


# Ejercicio 6
nums = [1, 2, 3, 4, 5, 6, 7]
rotada = [nums[-1]] + nums[0:-1]
print("Lista rotada:", rotada)


# Ejercicio 7
temperaturas = [
    [12, 25], [14, 27], [13, 23],
    [15, 29], [11, 21], [10, 19], [13, 24]
]

prom_min = sum([min(t) for t in temperaturas]) / len(temperaturas) # Encontre esta forma de iterar  sin la necesidad de hacer mas lineas de codigo, simplemente itero y guardo el resultado que me interesa en cada iteración
prom_max = sum([max(t) for t in temperaturas]) / len(temperaturas)
print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)

amplitudes = [max(t) - min(t) for t in temperaturas]
dia_max_amp = amplitudes.index(max(amplitudes)) + 1 # agarro el indice y le sumo 1 para que el día empiece en 1
print("Mayor amplitud térmica en día:", dia_max_amp)


# Ejercicio 8
notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 10, 8],
    [4, 5, 6],
    [8, 7, 9]
]

# Promedio por estudiante
for i, fila in enumerate(notas): # enumerate trae el indice y el valor de la fila
    print(f"Promedio estudiante {i+1}:", sum(fila)/len(fila))

# Promedio por materia
for j in range(len(fila)):
    materia = [notas[l][j] for l in range(len(notas))]
    print(f"Promedio materia {j+1}:", sum(materia)/len(materia))


# Ejercicio 9
tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def mostrar_tablero(): # Creo la función para no repetir codigo
    for fila in tablero:
        print(" ".join(fila))

for turno in range(9): # Maximo 9 turnos
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
    fila = int(input(f"Jugador {jugador}, ingrese fila (1-3): "))
    col = int(input(f"Jugador {jugador}, ingrese columna (1-3): "))
    if tablero[fila - 1][col -1] == "-":
        tablero[fila -1][col -1] = jugador
    mostrar_tablero()


# Ejercicio 10
ventas = [
    [10, 12, 5, 7, 20, 15, 9],  
    [8, 14, 6, 11, 13, 17, 10],  
    [20, 18, 22, 25, 21, 19, 23],
    [5, 9, 12, 8, 10, 7, 11]     
]

# 1) Total vendido por cada producto
print("Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

# 2) Día con mayores ventas totales
totales_dias = []
for j in range(len(ventas[i])):
    total_dia = sum(ventas[i][j] for i in range(4))
    totales_dias.append(total_dia)

dia_max = totales_dias.index(max(totales_dias)) + 1
print(f"El día con mayores ventas totales fue el día {dia_max} con {max(totales_dias)} ventas.")

# 3) Producto más vendido en la semana
producto_max = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_max} con {max(totales_productos)} ventas.")

