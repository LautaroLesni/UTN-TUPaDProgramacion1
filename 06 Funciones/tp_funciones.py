import math

# 1. Imprimir Hola Mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludar usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Área y perímetro del círculo
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida"
    return suma, resta, multiplicacion, division

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def main():
    imprimir_hola_mundo()
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    radio = float(input("Ingrese el radio de un círculo: "))
    print("Área:", calcular_area_circulo(radio))
    print("Perímetro:", calcular_perimetro_circulo(radio))

    segundos = int(input("Ingrese una cantidad de segundos: "))
    print("Equivalen a horas:", segundos_a_horas(segundos))

    numero = int(input("Ingrese un número para su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, multi, div = operaciones_basicas(a, b)
    print("Suma:", suma, "Resta:", resta, "Multiplicación:", multi, "División:", div)

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print("Su IMC es:", round(calcular_imc(peso, altura), 2))

    temp_c = float(input("Ingrese temperatura en Celsius: "))
    print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(temp_c))

    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    print("El promedio es:", calcular_promedio(n1, n2, n3))

main()