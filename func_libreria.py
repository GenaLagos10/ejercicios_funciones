
def menu_principal():
    print("***Libreria EL LECTOR AGIL***")
    print()
    print("1. Añadir nuevo libro al catálogo")
    print("2. Actualizar stock de un libro existente")
    print("3. Ver catálogo completo")
    print("4. Salir")
    print()

def add_libro(catalogo_libros):

    while True:

        nombre_libro=input("Ingrese el nombre del libro a añadir: ")
        if nombre_libro in catalogo_libros:
            print("El libro ya está agregado")
            continue
        elif not nombre_libro:
            print("debe ingresar un nombre válido")
            continue
        else:
            break

    while True:

        autor=input("ingrese el autor del libro: ")
        if not autor:
            print("ingrese un nombre valido")
        else:
            break

    while True:

        try:
            precio=int(input("ingrese el precio de libro: "))
            stock=int(input("Ingrese el stock inicial del libro: "))
        except ValueError:
            print("ingrese un valor numérico")

        if (precio > 0) and (stock >0):
            break
        else:
            print("el precio y stock deben ser mayor a 0")

    catalogo_libros[nombre_libro]={

        "autor":autor,
        "stock":stock,
        "precio":precio
    }

def actualizar_stock(catalogo_libros):

    while True:

        stock_titulo=input("ingrese el titulo a actualizar stock: ")
        if stock_titulo in catalogo_libros:

            nuevo_stock=catalogo_libros[stock_titulo] #esto deberia contener los datos stock, autor, precio

            ingresar_nuevo_stock=int(input("ingrese el nuevo stock: "))

            if ingresar_nuevo_stock > 0:
                nuevo_stock["stock"]=nuevo_stock["stock"]+ingresar_nuevo_stock
                break
            else:
                print("debe ingresar un numero mayor que 0")
                continue
        else:
            print("el libro no está en el catálogo")
            continue

def ver_catalogo(catalogo_libros):

    if not catalogo_libros:
        print("el catálogo está vacio")
        
    for titulo, detalles in catalogo_libros.items():
        print(f"\nTítulo: {titulo}")
        print(f"  Autor: {detalles['autor']}")
        print(f"  Precio: ${detalles['precio']:.2f}")
        print(f"  Stock: {detalles['stock']} unidades")
    print("--------------------------")

def main():

    
    catalogo_libros = {
        "Cien años de soledad": {"autor": "Gabriel García Márquez", "precio": 15.50, "stock": 10},
        "1984": {"autor": "George Orwell", "precio": 12.00, "stock": 15},
        "Don Quijote de la Mancha": {"autor": "Miguel de Cervantes", "precio": 20.00, "stock": 5}
}

    while True:

        menu_principal()


        try:
            op=int(input("elige entre las opciones: 1,2,3 o 4: "))

            if op in [1,2,3,4]:
                
                    if op ==1:
                        add_libro(catalogo_libros)
                    elif op ==2:
                        actualizar_stock(catalogo_libros)
                    elif op ==3:
                        ver_catalogo(catalogo_libros)
                    elif op ==4:
                        print("Hasta luego")
                        break  
            else:
                print("ingrese un valor válido")
            
        except ValueError:
                    print("ingresa un valor numérico")      
         
main()