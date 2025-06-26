
# * MENU PRINCIPAL *
def mostrar_menu():
    print()
    print("\n--- MENÚ PRINCIPAL ---")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    print("----------------------")

# 1.- * REGISTRO DE USUARIOS *
def ingreso_usuarios(usuario_registrado):

    #Nombre usuario
    while True:
        nombre_usuario=input("Ingrese su nombre de usuario: ").strip()
        if not nombre_usuario:
            print("el nombre de usuario no puede estar vacio")  
        elif nombre_usuario in usuario_registrado:
            print("El nombre de usuario ya existe. Ingrese otro")
        else:
            break
    #Sexo usuario
    while True:
        sexo=input("Ingrese su sexo (F/M): ").strip().upper()
        if sexo not in ["F", "M"]:
            print("Debe elegir entre F y M")
        else:
            break
    #Contraseña usuario
    while True:
        password=input("Ingrese su contraseña: ").strip()
        #validacion largo contraseña
        if len(password) < 8:
            print("Error. La contraseña debe contener al menos 8 carácteres")
            continue
        #Validacion si tiene numeros
        tiene_numero=False
        for char in password:
            if char.isdigit():
                tiene_numero=True
                break
        if not tiene_numero:
            print("La contraseña debe contener al menos un número")
            continue
        #Validacion si tiene letras
        tiene_letra=False
        for char in password:
            if char.isalpha():
                tiene_letra=True
                break
        if not tiene_letra:
            print("Error. la contraseña debe contener al menos una letra")
            continue
        #Validacion si no contiene espacios
        if " " in password:
            print("La contraseña no puede contener espacios")
            continue

        break
    #Diccionario anidado
    nuevo_usuario= {
        "sexo":sexo,
        "password": password

    }

    usuario_registrado[nombre_usuario] = nuevo_usuario
    print(f"\nUsuario '{nombre_usuario}' ingresado exitosamente.")
    return True

#2.- * BUSQUEDA DE USUARIOS *      
def buscar_usuario(usuario_registrado):
    print("\n--- Búsqueda de Usuario ---")

    nombre_usuario_buscar=input("Ingrese el nombre de usuario a buscar: ")

    if nombre_usuario_buscar in usuario_registrado:

        #"usuario_encontrado"contiene ahora el dato (sexo y contraseña) ya que
        # con "usuario_registrado[nombre_usuario_buscar]" se invoca, a traves
        # del nombre de usuario a buscar (clave), el diccionario que los contiene.
        usuario_encontrado = usuario_registrado[nombre_usuario_buscar] 
        print(f"\nUsuario encontrado:")
        print()
        print(f"    Nombre de usuario: {nombre_usuario_buscar}") 
        print(f"    Sexo: {usuario_encontrado["sexo"]}")
        print(f"    Contraseña: {usuario_encontrado["password"]}")
    
    else:
        print("El nombre de usuario no se encuentra registrado")

# 3.- * BORRAR USUARIOS *
def borrar_usuario(usuario_registrado):
    print("\n--- Borrar usuario ---")

    nombre_usuario_borrar=input("Ingrese el nombre de usuario a borrar: ")

    if nombre_usuario_borrar in usuario_registrado:
        print(f"Usuario {nombre_usuario_borrar} borrado exitosamente")
        del usuario_registrado[nombre_usuario_borrar]

    else:
        print(f"No se pudo eliminar el usuario. El usuario {nombre_usuario_borrar} no existe")

# * FUNCION PRINCIPAL * 
def main():
    usuarios = {}

    while True:
        mostrar_menu()
        op=input("ingrese una opcion 1/2/3/4: ")

        if op == "1":
            ingreso_usuarios(usuarios)
        elif op == "2":
            buscar_usuario(usuarios)
        elif op == "3":
            borrar_usuario(usuarios)
        elif op == "4":
            print("Hasta pronto!")
            break
        else:
            print("Opción no válida. Ingrese un numero del 1 al 4")


main()

