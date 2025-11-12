import string

# Ejercicio 1
print("EJERCICIO 1")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# Ejercicio 2
print("\nEJERCICIO 2")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# Ejercicio 3
print("\nEJERCICIO 3")
frutas = list(precios_frutas.keys())
print(frutas)

# Ejercicio 4
print("\nEJERCICIO 4")
agenda = {}
for i in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese número telefónico: ")
    agenda[nombre] = numero

consulta = input("Ingrese un nombre para consultar su número: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# Ejercicio 5
print("\nEJERCICIO 5")
frase = input("Ingrese una frase: ")
frase = frase.lower()
palabras = frase.split()

palabras_unicas = set(palabras)
conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo_palabras)

# Ejercicio 6
print("\nEJERCICIO 6")
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")

# Ejercicio 7
print("\nEJERCICIO 7")
parcial1 = set(input("Ingrese los alumnos que aprobaron el Parcial 1 (separados por espacio): ").split())
parcial2 = set(input("Ingrese los alumnos que aprobaron el Parcial 2 (separados por espacio): ").split())

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Ejercicio 8
print("\nEJERCICIO 8")
stock = {"lapicera": 20, "cuaderno": 35, "regla": 10}

producto = input("Ingrese el producto a consultar o agregar: ").lower()
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Ejercicio 9
print("\nEJERCICIO 9")
agenda_eventos = {
    ("lunes", "09:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de programación",
    ("miércoles", "10:00"): "Laboratorio"
}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")

evento = agenda_eventos.get((dia, hora))
if evento:
    print(f"Actividad: {evento}")
else:
    print("No hay actividades en ese horario.")

# Ejercicio 10
print("\nEJERCICIO 10")
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

invertido = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido (capital -> país):", invertido)
