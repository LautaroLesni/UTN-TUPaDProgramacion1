import sys


def factorial(n):
    if n < 0:
        raise ValueError("factorial no definido para negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("fibonacci no definido para negativos")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(base, exponente):
    if exponente < 0:
        # para este TP tratamos solo exponentes enteros no negativos
        raise ValueError("exponente negativo no soportado en esta versión")
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def decimal_a_binario(n):
    if n < 0:
        raise ValueError("solo números enteros no negativos")
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n < 0:
        n = -n  
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    if numero < 0:
        numero = -numero
    if digito < 0 or digito > 9:
        raise ValueError("digito debe estar entre 0 y 9")
    if numero == 0:
        return 1 if digito == 0 else 0
    def helper(n, d):
        if n == 0:
            return 0
        return (1 if (n % 10) == d else 0) + helper(n // 10, d)
    return helper(numero, digito)


def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            s = input(prompt).strip()
            val = int(s)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Por favor ingresá un entero entre {min_val} y {max_val}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Ingresá un número entero.")

def normalizar_palabra(s):
    s = s.replace(" ", "").lower()
    accents = str.maketrans("áéíóúÁÉÍÓÚüÜ", "aeiouAEIOUuU")
    s = s.translate(accents)
    return s


def main():
    print("TP - Recursividad (ejecución interactiva)\n")

    # Ejercicio 1
    n = input_int("1) Ingresá un número entero positivo N para mostrar factoriales: ", min_val=1)
    print(f"Factoriales desde 1 hasta {n}:")
    for i in range(1, n + 1):
        print(f"{i} = {factorial(i)}")

    # Ejercicio 2
    m = input_int("\n2) Ingresá la posición M (entero >= 0) para mostrar Fibonacci: ", min_val=0)
    print(f"Serie de Fibonacci hasta la posición {m}:")
    for i in range(0, m + 1):
        print(fibonacci(i), end=" ")
    print()

    # Ejercicio 3
    base = None
    while True:
        try:
            base = float(input("\n3) Ingresá la base (número, puede ser decimal): ").strip())
            break
        except ValueError:
            print("Entrada inválida. Ingresá un número (ej: 2 o 3.5).")
    exp = input_int("Ingresá el exponente (entero no negativo): ", min_val=0)
    try:
        print(f"{base}^{exp} = {potencia(base, exp)}")
    except ValueError as e:
        print("Error:", e)

    # Ejercicio 4
    d = input_int("\n4) Ingresá un entero no negativo para convertir a binario: ", min_val=0)
    print(f"{d} en binario -> {decimal_a_binario(d)}")

    # 5) Ejercicio 5
    raw = input("\n5) Ingresá una palabra (si tiene espacios/acentos serán normalizados automáticamente): ").strip()
    palabra = normalizar_palabra(raw)
    print(f"Palabra normalizada: '{palabra}'")
    print("Es palíndromo?" , es_palindromo(palabra))

    # Ejercicio 6
    s_num = input_int("\n6) Ingresá un entero positivo para sumar sus dígitos: ", min_val=0)
    print(f"Suma de dígitos de {s_num} -> {suma_digitos(s_num)}")

    # Ejercicio 7
    bloques = input_int("\n7) Ingresá la cantidad de bloques del nivel más bajo (N >= 1): ", min_val=1)
    print(f"Total de bloques necesarios -> {contar_bloques(bloques)}")

    # Ejercicio 8
    numero = input_int("\n8) Ingresá un número entero positivo donde buscar el dígito: ", min_val=0)
    dig = input_int("Ingresá el dígito a contar (0..9): ", min_val=0, max_val=9)
    print(f"El dígito {dig} aparece {contar_digito(numero, dig)} vez/veces en {numero}.")

    print("\nFin del TP. ¡Listo!")

if __name__ == "__main__":
    try:
        main()
    except RecursionError:
        print("Error: Recursión demasiado profunda para los valores ingresados.", file=sys.stderr)
    except Exception as e:
        print("Ha ocurrido un error:", e, file=sys.stderr)
