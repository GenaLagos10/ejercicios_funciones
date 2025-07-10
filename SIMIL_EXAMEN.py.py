productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                           }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print()
    print("1.- Stock marca")
    print("2.- Busqueda por RAM y precio")
    print("3.- Eliminar producto")
    print("4.- Salir.")
    print("----------------------")

def stock_marca(marca):
    stock_total=0
    marca_existe = False

    for modelo, detalles in productos.items():
        if detalles[0].lower() == marca.lower():
            if modelo in stock:
                stock_total+=stock[modelo][1]
                marca_existe= True

    if marca_existe:
        print(f"El stock de {marca} es: {stock_total}")

    elif not marca_existe:
        print("La marca ingresada no está en el catálogo")

def busqueda_ram_precio(ram_min, ram_max, precio):
    encontrados= False
    for modelo, detalles in productos.items():
        if modelo in stock and stock[modelo][1] > 0:
            ram_producto=int(detalles[2].replace('GB', ''))
            if ram_min <= ram_producto <= ram_max and stock[modelo][0] <= precio:
                print(f"Modelo: {modelo} -> {detalles}")     
                encontrados = True    

    if not encontrados:
        print("No se encontraron modelos con esas características")

def eliminar_producto(modelo):
    global productos
    global stock

    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        return True
       
    else:
        return False

def main():

    while True:
        mostrar_menu()

        op = input("Ingrese una opción 1/2/3/4: ")
        
        if op == "1":
            marca_input=input("Ingresa una marca: ").strip().lower()
            stock_marca(marca_input)

        elif op == "2":
            while True:
                try:
                    ram_min_input=int(input("ingrese la ram mínima: "))
                    ram_max_input=int(input("Ingrese la ram máxima: "))
                    precio_input=int(input("Ingrese el precio máximo "))
                    busqueda_ram_precio(ram_min_input, ram_max_input, precio_input)
                    break
                except ValueError:
                    print("Ingrese un número entero.")
                    
        elif op == "3":
            while True:
                modelo_input=input("ingrese un modelo: ").upper()
                if eliminar_producto(modelo_input):
                    print("producto eliminado con exito")
                
                else:
                    print("el producto no se ha podido eliminar")
                
                continuar=input("¿desea borrar otro modelo? (si/no): ").lower()
                if continuar != "si":
                    break

        elif op == "4":
            print("Adios")
            break
        else:
            print("Debe ingresar una opcion valida")
            continue

main()

                