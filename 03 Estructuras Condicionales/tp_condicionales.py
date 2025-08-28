""" TP Condicionales """
# Ejercicio 1
edad = int(input('Ingrese su edad '))
if edad >= 18:
    print("Es mayor de edad.")

# Ejercicio 2
nota = float(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

# Ejercicio 3
numeroPar = float(input('Ingrese un número par: '))
if numeroPar % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingrese un número par')

# Ejercicio 4
edad = int(input('Ingrese su edad: '))
if edad < 12 and edad > 0:
    print('Pertenece a la categoría niño')
elif edad >= 12 and edad < 18:
    print('Pertenece a la categoría adolescente')
elif edad >= 18 and edad < 30:
    print('Pertenece a la categoría adulto joven')
elif edad > 30:
    print('Adulto')
else: 
    print('Tu edad no entra dentro de las categorias')

# Ejercicio 5
password = input('Ingrese una contraseña: ')
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print (numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"moda: {moda}, mediana: {mediana}, media: {media}")
if media > mediana and mediana > moda:
    print('Sesgo positivo o a la derecha')
elif media < mediana and  mediana < moda:
    print('Sesgo negativo o a la izquierda')
elif media == mediana and mediana == moda:
    print('Sin sesgo')
else:
    print('No aplica')

# Ejercicio 7

palabra = input ('Escriba su palabra: ')
vocales = ['a','e','i','o','u']
letra_final = palabra[len(palabra) -1]
palabra_final = ''
if letra_final in vocales:
    palabra_final = palabra + '!'
else:
    palabra_final = palabra
print(palabra_final)

# Ejercicio 8

nombre = input('Ingrese su nombre: ')
option = int(input('Ingrese su opción (del 1 al 3): '))
if option < 1 or option > 3:
    print('Opción fuera de rango')
else:
    if option == 1:
        print(nombre.upper())
    elif option == 2:
        print(nombre.lower())
    else:
        print(nombre.title())

# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# Ejercicio 10

hemisferio = input('Ingrese su hemisferio (norte/sur): ')
if hemisferio != 'norte' and hemisferio != 'sur':
    print('Hemisferio incorrecto')
else:
    mes = int(input('Ingrese el mes actual (en número EJ: 1 (Enero)): '))
    dia = int(input('Ingrese el dia actual (en número): '))
    if (mes < 1 or mes > 12) or (dia < 0 or dia > 31):
        print('Fecha fuera de rango')
    else:
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion_norte = "Invierno"
            estacion_sur = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion_norte = "Primavera"
            estacion_sur = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion_norte = "Verano"
            estacion_sur = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion_norte = "Otoño"
            estacion_sur = "Primavera"

        if hemisferio == 'norte':
            print(f"En el hemisferio norte, ahora es {estacion_norte}.")
        else:
            print(f"En el hemisferio sur, ahora es {estacion_sur}.")