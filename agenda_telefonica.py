
def mostrar_menu():
    print("\n--- MI CONTACTO RAPIDO ---")
    print()
    print("1.- Añadir nuevo contacto")
    print("2.- Actualizar numero de contacto")
    print("3.- Eliminar contacto")
    print("4.- Ver todos los contactos")
    print("5.- Salir.")
    print("----------------------")

def añadir_contacto(diccionario_contactos):

    while True:
        nombre=input("Ingrese su nombre: ").strip()
        if not nombre:
            print("Debe ingresar un nombre")
            continue
        elif nombre in diccionario_contactos:
            print("El nombre de contacto ya existe. Ingrese otro")
            continue
        else:
            break

    while True:
        numero_telefono=input("ingrese un numero de telefono: ").strip()
        if not numero_telefono:
            print("debe ingresar un número de telefono válido")
        elif numero_telefono.isdigit():
            break
        else:
            print("entrada inválida. Debe ingresar solo números")

    diccionario_contactos[nombre]=numero_telefono

def actualizar_num(diccionario_contactos):
    while True:
        nom_contacto=input("ingrese el nombre del contacto: ").strip()
        if nom_contacto not in diccionario_contactos:
            print("el nombre no existe. Primero debe agregarlo")

        else:
            nuevo_numero=input("Ingrese el nuevo numero: ").strip
            if not nuevo_numero:
                print("el numero no puede estar vacio")
                continue
            elif nuevo_numero.isdigit():
                diccionario_contactos[nom_contacto]=nuevo_numero
                print("Número cambiado con éxito")
                break

def eliminar_contacto(diccionario_contactos):

    while True:
        contacto_eliminar=input("Ingrese el nombre del contacto a eliminar: ")

        if contacto_eliminar not in diccionario_contactos:
            print("El contacto no se puede eliminar ya que no existe")
            break #break aquí para no obligar al usuario a eliminar un numero. Si de todos modos quiere eliminar alguno, vuelve a entrar a la opción.
        else:
            del diccionario_contactos[contacto_eliminar]
            print("contacto eliminado con éxito")
            break

def ver_contactos(diccionario_contactos):

    if not diccionario_contactos:
        print("La agenda telefónica está vacia.")
    
    else:

        for nom, num in diccionario_contactos.items():
            print(f"Nombre de contacto: {nom}")
            print(f"Numero telefónico: {num}")
            print("-------------------------------------")

def main():

    agenda_contactos={}

    while True:
        mostrar_menu()

        try:

            op=int(input("Ingrese una opcion del 1 al 5: "))
            if op in [1,2,3,4,5]:

                if op == 1:
                    añadir_contacto(agenda_contactos)
                elif op ==2:
                    actualizar_num(agenda_contactos)
                elif op ==3:
                    eliminar_contacto(agenda_contactos)
                elif op ==4:
                    ver_contactos(agenda_contactos)
                elif op ==5:
                    print("Hasta pronto!")
                    break
            else:
                print("La opción ingresada no es válida")
                continue

        except ValueError:
            print("Debe ingresar un valor numérico")

main()      





