import time

productos = {
    'MX100': ['microondas', 'Samsung', 1000, 'blanco', 'A', 24],
    'BL200': ['licuadora', 'Oster', 800, 'rojo', 'B', 12],
    'TP300': ['tostadora', 'Philips', 650, 'negro', 'A', 18],
    'MX150': ['microondas', 'Daewoo', 1100, 'gris', 'C', 24],
    }

stock = {
    'MX100': [79990, 4],
    'BL200': [45990, 10],
    'TP300': [27990, 0],  # sin stock
    'MX150': [89990, 2],
}

def menu():
    print()
    print("*** MENU PRINCIPAL ***")
    print("1. Ver stock por tipo de producto")
    print("2. Buscar por rango de potencia y eficiencia")
    print("3. Eliminar un producto")
    print("4. Salir")
    print()

def stock_tipo(tipo):
    stock_total=0
    encontrado= False

    for clave, valor in productos.items():
        if clave in stock and stock[clave][1] > 0:
            if tipo.lower() == valor[0].lower():
                stock_total+=stock[clave][1]
                encontrado=True
    if encontrado:          
        print(f"El stock para {tipo.lower()} es de: {stock_total} unidades")       

    if not encontrado:
        print("No hay productos que mostrar.")
    time.sleep(2)

def buscar_potencia_eficiencia(pot_min, pot_max, eficiencia):
    encontrado= False

    for clave, valor in productos.items():
        if clave in stock and stock[clave][1] > 0:
            potencia=valor[2]
            if pot_min <= potencia <=pot_max and eficiencia.upper() == valor[4]:
                print(f"{clave} -> {valor}")
                encontrado=True
    
    if not encontrado:
        print("No hay productos que mostrar.")
        time.sleep(2)

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
        op = input("Ingrese una opcion (1/2/3/4): ")

        if op == "1":
            tipo= input("Ingrese el tipo de producto: ").strip()
            stock_tipo(tipo)

        elif op == "2":
            while True:
                try:
                    pot_min=int(input("Ingrese la potencia mínima que desea: "))
                    pot_max=int(input("Ingrese la potencia máxima que desea: "))
                    eficiencia=input("Ingrese la eficiencia (A/B/C): ").upper()
                    buscar_potencia_eficiencia(pot_min, pot_max, eficiencia)
                    break
                except ValueError:
                    print("Ingrese un valor numérico")
                    time.sleep(2)
        
        elif op == "3":
            while True:
                codigo= input("Ingrese el codigo del producto que desea eliminar: ").upper().strip()
                if eliminar_producto(codigo):
                    print("Producto eliminado!!")
                    time.sleep(2)
                else:
                    print("El producto no existe!!")
                    time.sleep(2)
                    
                continuar=input("¿quiere eliminar otro producto? (si / no): ")
                if continuar != "si":
                    break

        elif op == "4":
            print("Programa finalizado ")
            time.sleep(1)
            break

        else:
            print("debe ingresar una opcion válida (1/2/3/4)")
            time.sleep(2)

main()