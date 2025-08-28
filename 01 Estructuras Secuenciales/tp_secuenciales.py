""" TP Secuenciales """
# Ejercicio 1
print('Hola mundo!')

# Ejercicio 2
nombre = input('Ingrese su nombre ')
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input('Ingrese su nombre ')
apellido = input('Ingrese su apellido ')
edad = input('Ingrese su edad ')
pais = input('Ingrese su país ')
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

# Ejercicio 4
pi = 3.14159
radio = float(input('Ingrese el radio del circulo: '))
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5
segundos = int(input('Ingrese una cantidad de segundos: '))
minutos = segundos / 60
horas = minutos / 60
print(f"{segundos} segundos son {horas} horas")

# Ejercicio 6
number = int(input('Ingrese un número entero: '))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Ejercicio 7
number1 = int(input('Ingrese el primer número entero: '))
number2 = int(input('Ingrese el segundo número entero: '))
if number1 < 1 or number2 < 1:
    print("Error: Ambos números deben ser mayores que 0.")
suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2
division = number1 / number2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Ejercicio 8
altura = float(input('Ingrese la altura en metros: '))
peso = float(input('Ingrese el peso en kilogramos: '))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

# Ejercicio 9
temperaturaCelsius = float(input('Ingrese la temperatura en grados Celsius: '))
temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {temperaturaFahrenheit}")

# Ejercicio 10
numero1= float(input('Ingrese el primer número: '))
numero2= float(input('Ingrese el segundo número: '))
numero3= float(input('Ingrese el tercer número: '))
promedio = (numero1 + numero2 + numero3) / 3
print (f"El promedio de los números es: {promedio}")