productos = {
    'RF100': ['refrigerador', 'LG', 'WiFi', 'plata', 150, 24],
    'HR200': ['horno', 'Samsung', 'Bluetooth', 'negro', 1800, 12],
    'LV300': ['lavadora', 'Bosch', 'WiFi', 'blanco', 1200, 36],
    'HR150': ['horno', 'Midea', 'Ninguna', 'gris', 1600, 18]
}

stock = {
    'RF100': [499990, 3],
    'HR200': [299990, 0],  # sin stock
    'LV300': [459990, 2],
    'HR150': [219990, 5]
}

def menu():
    print("----------------------------------------------")
    print("*** MENÚ ELECTROSMART ***")
    print("----------------------------------------------")
    print("1. Ver stock por tipo")
    print("2. Buscar por conectividad y consumo máximo")
    print("3. Eliminar un producto")
    print("4. Salir")
    print("----------------------------------------------")

def stock_tipo(tipo):
    encontrado=False
    stock_total=0

    for clave, datos in productos.items():
        if clave in stock and stock[clave][1] > 0:
            if tipo.lower() == datos[0].lower():
                stock_total+=stock[clave][1]
                encontrado=True

    if encontrado:
        print(f"El stock para {tipo} es de: {stock_total} unidades")
    else:
        print(f"No se encontró stock para: {tipo}")

def buscar_conectividad_consumo(conectividad, consumo_max):
    encontrado=False

    for clave, datos in productos.items():
        if clave in stock and stock[clave][1] > 0:
            if conectividad.lower() == datos[2].lower():
                if consumo_max >= datos[4]:
                    print(f"producto: {clave} -> {datos} precio: {stock[clave][0]}")
                    encontrado = True
    if not encontrado:
        print("No se encontraron coincidencias para los parámetros ingresados")

def eliminar_producto(codigo):

    if codigo in productos and codigo in stock:
        del productos[codigo]
        del stock[codigo]
        return True
    else:
        return False

def main():

    while True:
        menu()
        op=input("Ingrese una opcion (1/2/3/4): ")

        if op == "1":

            tipo=input("ingrese el tipo de electrodomestico que busca: ").lower()
            stock_tipo(tipo)

        elif op == "2":
            while True:

                conectividad=input("Ingrese la conectividad que desea: ").strip().lower()
                try:
                    consumo_max=int(input("Ingrese el consumo máximo: "))
                    buscar_conectividad_consumo(conectividad, consumo_max)
                    break
                except ValueError:
                    print("Ingrese un valor numérico")

        elif op == "3":
            while True:
                codigo=input("Ingrese el código del producto que desea borrar: ").upper()

                if eliminar_producto(codigo):
                    print("Producto eliminado con éxito")
                else:
                    print("El codigo ingresado no es válido")
                
                continuar=input("¿Desea eliminar otro producto? si/no")
                if continuar != "si":
                    break

        elif op == "4":
            print("Saliendo del programa")
            break
        else:
            print("Ingresa una opción válida: (1/2/3/4)")
            continue

main()
