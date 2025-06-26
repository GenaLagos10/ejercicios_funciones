import time

def mostrar_menu():
    print()
    print("\n--- MENÚ PRINCIPAL ---")
    print()
    print("1.- Comprar entradas.")
    print("2.- Verificar compra.")
    print("3.- Cancelar compra.")
    print("4.- Salir.")
    print("----------------------")

def comprar_entradas(stock, diccionario_clientes):
    while True:

        #validacion nombre de usuario
        nombre_usuario=input("Ingrese su nombre de usuario: ").strip()
        if not nombre_usuario:
            print("debe ingresar un nombre de usuario válido")
            continue
        else:
            break
    
    while True:

        #validacion codigo secreto
        codigo_secreto=input("Ingrese el codigo secreto: ").strip()
        if codigo_secreto == "ROCK2025":
            break
        else:
            print("debe ingresar un código válido")
            continue
    
    while True:
        #validacion cantidad de entradas
        try:

            cantidad_entradas=int(input("Ingrese la cantidad de entradas a comprar (5 máximo): "))

        except ValueError:
            print("Ingrese un valor numérico")

        if 0 < cantidad_entradas <= 5 and cantidad_entradas <= stock:
            print(f"La cantidad de entradas compradas es: {cantidad_entradas} entradas")
            break
        else:
            print(f"la cantidad a comprar es de 1 a 5 entradas. Las entradas restantes son {stock}")
            continue
    
#si todo esto se cumple, vamos a hacer efectivo el ingreso del usuario y las entradas
#ingreso de nombre, de cantidad de entradas, y descontar entradas del stock

    diccionario_clientes[nombre_usuario]=cantidad_entradas
    stock=stock-cantidad_entradas

    return stock, diccionario_clientes

def verificar_compra(stock, diccionario_clientes):

    while True:

        nombre_verificar=input("ingrese su nombre: ")
        if nombre_verificar in diccionario_clientes:
            #"cliente verificado" es el valor del codigo.
            cliente_verificado= diccionario_clientes[nombre_verificar]
            print(f"Nombre de usuario:  {nombre_verificar}")
            print(f"Cantidad de entradas adquiridas: {cliente_verificado}")
            print(f"Stock actual de entradas: {stock}")
            break
        else:
            print("El usuario ingresado no ha realizado compra de entradas")
            break
        
    return stock, diccionario_clientes
    
def cancelar_compra(stock, diccionario_clientes):

    while True:

        nombre_cancelar=input("Ingrese el nombre de usuario para cancelar: ")
        if nombre_cancelar in diccionario_clientes:
            cancelacion_compra=diccionario_clientes[nombre_cancelar]
            del diccionario_clientes[nombre_cancelar]
            stock=stock+cancelacion_compra
            print("compra cancelada con éxito")
            break
        else:
            print("El nombre ingresado no está registrado")
            break
    return stock, diccionario_clientes

def main():
    diccionario_clientes={}
    stock=50

    while True:
        mostrar_menu()

        try:
            op=int(input("Ingrese una opcion: 1/2/3/4: "))
            if op in [1,2,3,4]:

                if op == 1:
                    stock, diccionario_clientes = comprar_entradas(stock, diccionario_clientes)
                elif op == 2:
                  stock, diccionario_clientes = verificar_compra(stock, diccionario_clientes)
                elif op == 3: 
                    stock, diccionario_clientes = cancelar_compra(stock, diccionario_clientes)
                elif op == 4:
                    print("Gracias. Adios")
                    break
            else:
                print("debe ingresar un opción del 1 al 4")
                continue
        except ValueError:
            print("Ingrese un valor numérico válido")

if __name__ == "__main__":
    main()
            

