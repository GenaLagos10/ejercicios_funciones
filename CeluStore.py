# productos = {modelo: [marca, tamaño_pantalla, RAM, almacenamiento, procesador, cámara], ...}

productos = {
    'A51': ['Samsung', 6.5, '4GB', '128GB', 'Exynos 9611', '48MP'],
    'MI10': ['Xiaomi', 6.7, '8GB', '128GB', 'Snapdragon 865', '108MP'],
    'IP11': ['Apple', 6.1, '4GB', '64GB', 'A13 Bionic', '12MP'], #sin stock
    'G8P': ['Motorola', 6.4, '4GB', '64GB', 'Snapdragon 665', '16MP'],
    'N7P': ['Nokia', 6.3, '6GB', '128GB', 'Snapdragon 660', '48MP'],
    'A12': ['Samsung', 6.5, '3GB', '32GB', 'Helio P35', '13MP'],
}

# stock = {modelo: [precio, stock], ...}

stock = {
    'A51': [299990, 5],
    'MI10': [499990, 3],
    'IP11': [699990, 0], #sin stock
    'G8P': [199990, 12],
    'N7P': [259990, 4],
    'A12': [129990, 10],
}

def menu():

    print("*** MENU PRINCIPAL ***")
    print("----------------------------")
    print("1. Stock marca")
    print("2. Búsqueda por RAM y precio")
    print("3. Eliminar celular")
    print("4. Salir")
    print("----------------------------")

def stock_marca(marca):

    stock_total=0
    encontrados=False

    for id, datos in productos.items():
        if datos[0].lower() == marca.lower():
            stock_total=stock_total + stock[id][1]
            encontrados = True
    
    print(f"El stock de la marca {marca} es: {stock_total} unidades")

    if not encontrados:
        print("No existen productos de la marca ingresada.")

def busqueda_ram_precio(ram_min, ram_max, precio):
    encontrados= False

    for id, datos in productos.items():
        if id in stock and stock[id][1] > 0:
            ram_producto=int(datos[2].replace('GB', ''))
            if ram_min <= ram_producto <= ram_max and stock[id][0] <= precio:
                print(f"Modelo: {id} -> {datos}")
                encontrados= True
    
    if not encontrados:
        print("No hay celulares que mostrar.")

def eliminar_producto(modelo):
    global productos
    global stock
    eliminado = False

    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        return True
    if not eliminado:
        return False

def main():

    while True:
        menu()

        op=input("Ingrese una opcion (1/2/3/4): ")
  
        if op == "1":
            marca_in=input("Ingrese una marca: ").strip().lower()
            stock_marca(marca_in)

        elif op == "2":

            while True:
                try:
                    ram_min=int(input("Ingrese una cantidad mínima de ram a buscar: "))
                    ram_max=int(input("Ingrese una cantidad máxima de ram a buscar: "))
                    precio=int(input("Ingrese un precio tope: "))
                    busqueda_ram_precio(ram_min, ram_max, precio)
                    break
                except ValueError:
                    print("Ingrese un valor numérico")

        elif op == "3":
            while True:

                modelo=input("Ingrese el modelo a eliminar: ").strip().upper()
                resultado= eliminar_producto(modelo)

                if resultado:
                    print("Celular eliminado!!")
                else:
                    print("El modelo no existe!!")

                continuar=input("¿Desea eliminar otro celular? (si/no):").strip().lower()
                if continuar != "si":
                    break
                else:
                    continue
        elif op == "4":
            print("Programa finalizado")
            break

        else:
            print("Debe seleccionar una opción válida!!")
            continue

main()
