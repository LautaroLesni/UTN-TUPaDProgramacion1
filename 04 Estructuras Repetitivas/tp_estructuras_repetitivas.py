# Ejercicio 1
for i in range(0,101, 1):
    print(i)

# Ejercicio 2
numero = input("Ingrese un número entero: ")
print(len(numero))

# Ejercicio 3
inputNumberoUno = int(input("Ingrese un número entero: "))
inputNumberoDos = int(input("Ingrese otro número entero: "))
suma = 0
for i in range (inputNumberoUno + 1, inputNumberoDos, 1):
    suma += i

print(suma)

# Ejercicio 4
inputUsuario = ''
suma = 0
while inputUsuario != 0:
    if type(inputUsuario) == str:
        inputUsuario = int(input("Ingrese su primer número para sumar: "))
    else:
        inputUsuario = int(input("Ingrese otro número para sumar o 0 para finalizar: "))
    suma += inputUsuario

print(f"La suma total es: {suma}")

# Ejercicio 5
import random
numeroADivinar = random.randint(0, 9)
inputNumber = -1
while inputNumber != numeroADivinar:
    inputNumber = int(input("Adivine el número entre 0 y 9: "))
    if inputNumber < numeroADivinar:
        print("El número es mayor")
    elif inputNumber > numeroADivinar:
        print("El número es menor")
    else:
        print("¡Felicitaciones! ¡Adivinaste el número!")

# Ejercicio 6
for i in range(100, -2, -2):
    print(i)

# Ejercicio 7
inputUsuarioNumero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(0, inputUsuarioNumero + 1, 1):
    suma += i
print(f"La suma de los números desde 0 hasta {inputUsuarioNumero} es: {suma}") 

# Ejercicio 8
numerosImparesCount = 0
numerosParesCount = 0
numerosPositivosCount = 0
numerosNegativosCount = 0
for i in range(0, 100, 1):
    numeroOtorgadoPorElUsuario = int(input(f"Ingrese el número {i + 1}: "))
    if numeroOtorgadoPorElUsuario % 2 == 0:
        numerosParesCount += 1
    else:
        numerosImparesCount += 1
    if numeroOtorgadoPorElUsuario >= 0:
        numerosPositivosCount += 1
    else:
        numerosNegativosCount += 1
print(f"Números pares: {numerosParesCount}")
print(f"Números impares: {numerosImparesCount}")
print(f"Números positivos: {numerosPositivosCount}")
print(f"Números negativos: {numerosNegativosCount}")

# Ejercicio 9
from statistics import mean
numerosParaCalcularLaMedia = []
for i in range(0, 100, 1):
    numeroDadoPorelUsuario = int(input(f"Ingrese el número {i + 1}: "))
    numerosParaCalcularLaMedia.append(numeroDadoPorelUsuario)
media = mean(numerosParaCalcularLaMedia)
print(f"La media de los números ingresados es: {media}")

# Ejercicio 10

inputNumeroAInvertir = input("Ingrese un número: ")
numeroInvertido = ''
for i in range(len(inputNumeroAInvertir), 0, -1):
    numeroInvertido += inputNumeroAInvertir[i - 1]
print(f"El número invertido es: {numeroInvertido}")