

ARCHIVO_PRODUCTOS = "productos.txt"


# Ejercicio 2
def leer_y_mostrar_productos():
    productos = []
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea: 
                    nombre, precio, cantidad = linea.split(",")
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                    productos.append({
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    })
    except FileNotFoundError:
        print(f" El archivo '{ARCHIVO_PRODUCTOS}' no existe. Crealo antes de ejecutar el programa.")
        exit()
    return productos


# Ejercicio 3
def agregar_producto():
    print("\n--- Agregar nuevo producto ---")
    nombre = input("Ingrese nombre del producto: ").strip()
    precio = input("Ingrese precio del producto: ").strip()
    cantidad = input("Ingrese cantidad del producto: ").strip()

    with open(ARCHIVO_PRODUCTOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print(f" Producto '{nombre}' agregado correctamente.")


# Ejercicio 4
def cargar_productos_en_lista():
    productos = []
    with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos


# Ejercicio 5
def buscar_producto(productos):
    print("\n--- Buscar producto ---")
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ").strip()
    encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print(f"\n El producto '{nombre_buscar}' no se encuentra en la lista.")


# Ejercicio 6
def guardar_productos(productos):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("\n Archivo actualizado correctamente.")


def main():
    print("=== LISTA DE PRODUCTOS ===")
    productos = leer_y_mostrar_productos()

    agregar_producto()

    productos = cargar_productos_en_lista()

    buscar_producto(productos)

    guardar_productos(productos)


# Ejecutar el programa
if __name__ == "__main__":
    main()
