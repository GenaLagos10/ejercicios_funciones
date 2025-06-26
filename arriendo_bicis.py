dicc_usuarios={}
stock=15
import time

def mostrar_menu():
    print()
    print("\n--- ARRIENDO BICIS ---")
    print()
    print("1.- Arrendar bici.")
    print("2.- Buscar bici arrendada.")
    print("3.- Devolver bici.")
    print("4.- Salir.")
    print("----------------------")

def arrendar_bici():

    global stock
    global dicc_usuarios

    #while para validar nombre de usuario.
    while True:
        nombre_cliente=input("ingrese su nombre: ").strip()
        time.sleep(1)

        if nombre_cliente in dicc_usuarios or not nombre_cliente:
            print("debe ingresar otro nombre de usuario")
            time.sleep(1)
            continue
        else:
            break
    #while para validar cantidad de bicis
    while True:
        try:
            cantidad_arrendar=int(input("ingrese la cantidad que desea arrendar (Máximo 3): "))
            time.sleep(1)
        except ValueError:
            print("ingrese un valor valido numérico entre 1 y 3")
            time.sleep(1)
        
        if  0 < cantidad_arrendar <= 3 and stock >= cantidad_arrendar:
            time.sleep(1)
            break
        elif stock < cantidad_arrendar:
            print(f"Actualmente solo quedan {stock} bicicletas disponibles")
            time.sleep(1)
            continue
        else:
            print(f"Debes ingresar un numero entre 1 y 3")
            time.sleep(1)
            break
    #while para validar clave secreta
    while True:
        clave_secreta=input("Ingrese el codigo secreto para reservar: ")

        if clave_secreta == "RutaSegura2025":
            time.sleep(1)
            break
        else:
            print("Clave ingresada no es válida. Intente nuevamente")
            time.sleep(1)
            continue

    print(f" Sr/a {nombre_cliente}, ha arrendado con éxito {cantidad_arrendar} bicicletas")
    time.sleep(1)
    stock=stock - cantidad_arrendar 
    dicc_usuarios[nombre_cliente] = cantidad_arrendar
    return True

def buscar_arriendo_bicis():

    global stock
    global dicc_usuarios
    while True:

        buscar_reserva=input("ingrese su nombre de usuario: ").strip()
        if buscar_reserva in dicc_usuarios:
            #despues del if crear nueva variable donde se refiere al dicc[input_de_nombre]
            numero_bicis=dicc_usuarios[buscar_reserva]
            print(f"Usuario {buscar_reserva} encontrado. numero de bicis reservadas {numero_bicis}:")
            time.sleep(1)
            print(f"Stock actual: {stock} bicicletas.")
            time.sleep(1)
            break
            
        else:
            print("Ud. no tiene reservas")
            time.sleep(1)
            break

def devolver_bicileta():
    global stock
    global dicc_usuarios

    while True:
        devolucion_bici=input("Ingrese su nombre de usuario: ").strip()
        if devolucion_bici in dicc_usuarios:
            #despues del if, lo mismo que arriba: esta nueva variable se refiere al usuario especifico
            bicis_a_devolver=dicc_usuarios[devolucion_bici]
            del dicc_usuarios[devolucion_bici]
            stock+=bicis_a_devolver
            print(f"Usuario {devolucion_bici} encontrado. Devolución exitosa")
            time.sleep(1)
            print(f"Stock actual: {stock} bicicletas.")
            time.sleep(1)
            break
        else:
            print("Este usuario no está registrado")
            time.sleep(1)
            break
def main():
    while True:
        mostrar_menu()
        try:
            op=int(input("Ingrese una opcion del 1 al 4: "))

            if op in [1,2,3,4]:

                if op == 1:
                    arrendar_bici()
                elif op == 2:
                    buscar_arriendo_bicis()
                elif op == 3:
                    devolver_bicileta()
                elif op == 4:
                    print("Adios y gracias")
                    time.sleep(1)
                    break
            else:
                print("Ingrese un valor válido")
                time.sleep(1)
        except ValueError:
            print("Ingrese un valor numérico")
            time.sleep(1)

main()
