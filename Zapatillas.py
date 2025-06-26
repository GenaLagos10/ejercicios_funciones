#Sistema de venta de zapatillas
#Diccionario de datos para stock de zapatillas
import time

inventario= {
    "001": {"modelo":"Air Max", "precio":89990, "stock": 15},
    "002": {"modelo":"Classic", "precio":49990, "stock": 50},
    "003": {"modelo":"Runner", "precio":69990, "stock": 20},
    "004": {"modelo":"Basquet", "precio":79990, "stock": 5}
}

#Funcion para mostrar el inventario disponible
def mostrar_inventario():
    print("\n====INVENTARIO ZAPATILLAS===")
    print("Codigo | Modelo | Precio | Stock")
    print("--------------------------------")

    # ciclo for para iterar cada item del inventario
    for codigo, datos in inventario.items():
        print(f"{codigo}    |{datos["modelo"]:8}|  ${datos["precio"]}| {datos["stock"]}")

# * PROCESAR VENTA *
def procesar_venta():

    mostrar_inventario()

    #preguntar el codigo del producto a vender
    codigo = input("\nIngrese el codigo de la zapatilla: ")

    #validar que el codigo ingresado exista en el diccionario
    if codigo not in inventario:
        print("Error: el codigo ingresado no existe")
        return
    

    #solicitar la cantidad numerica a vender de zapatillas
    try:
        cantidad= int(input("Ingrese la catidad de zapatillas a vender: "))
    except ValueError:
        print("Error: debe ingresar un numero valido")
        return
    
    #validar que exista suficiente stock
    if cantidad <=0:
        print("Error: la cantidad debe ser mayor a 0")
        return
    elif cantidad > inventario[codigo]["stock"]:
        print("Error: No hay suficiente stock disponible.")
        return
    
    #calcular el valor de la venta
    precio_unitario = inventario[codigo]["precio"]
    total = precio_unitario * cantidad

    #actualizar el stock del diccionario inventario
    inventario[codigo]["stock"] -= cantidad

    # GENERAR BOLETA DE VENTA
    print("\n---BOLETA ELECTRONICA---")
    print(f"Producto: {inventario[codigo]['modelo']}")
    print(f"Precio unitario: ${precio_unitario} ")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: ${total}")
    print("---------------------------")
    print("Gracias por su compra!")

# ** FUNCION PRINCIPAL **
def main():
    print("BIENVENIDO AL SISTEMA DE SACATE LAS ZAPATILLAS")

    while True:
        print("\nOPCIONES")
        print()
        print("1.- Ver inventario")
        print("2.- Realizar ventas")
        print("3.- Salir")
        print()

        try:
            op= int(input("Seleccione una opcion: "))

            if op in [1,2,3]:

                if op==1:
                    mostrar_inventario()
                elif op ==2:
                    procesar_venta()
                elif op==3:
                    print("Saliendo del sistema...")
                    break
            else:
                print("Opción no valida. Vuelve a intentarlo")
                time.sleep(2)

        except ValueError:
            print("ingrese un valor válido")
            time.sleep(1)
        
main()