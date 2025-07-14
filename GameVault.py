juegos_catalogo = {
    'G001': ['The Witcher 3', 'CD Projekt Red', 'RPG', 'PC', 2015, 93],
    'G002': ['Red Dead Redemption 2', 'Rockstar Games', 'Aventura', 'PS4', 2018, 97],
    'G003': ['Minecraft', 'Mojang Studios', 'Sandbox', 'Multiplataforma', 2011, 82],
    'G004': ['Cyberpunk 2077', 'CD Projekt Red', 'RPG', 'PC', 2020, 86],
    'G005': ['God of War', 'Santa Monica Studio', 'Acción', 'PS4', 2018, 94],
    'G006': ['Animal Crossing: New Horizons', 'Nintendo', 'Simulación', 'Switch', 2020, 80],
    'G007': ['The Legend of Zelda: BOTW', 'Nintendo', 'Aventura', 'Switch', 2017, 97],
    'G008': ['Doom Eternal', 'id Software', 'FPS', 'PC', 2020, 88],
    'G009': ['Hades', 'Supergiant Games', 'Roguelike', 'PC', 2020, 93],
}

# inventario_tienda = {ID_juego: [copias_disponibles, precio_venta], ...]

inventario_tienda = {
    'G001': [10, 35990],
    'G002': [5, 42990],
    'G003': [25, 29990],
    'G004': [2, 39990],
    'G005': [0, 32990],  # Juego sin copias disponibles
    'G006': [15, 45990],
    'G007': [8, 48990],
    'G008': [3, 28990],
    'G009': [12, 25990],
}

def menu():
    print("--------------------------------------------------")
    print("*** MENÚ PRINCIPAL GAMEVAULT ***")
    print("--------------------------------------------------")
    print("1. Buscar juegos por Plataforma y Calificación.")
    print("2. Actualizar precio de juego.")
    print("3. Listar juegos por Desarrollador.")
    print("4. Salir.")
    print("--------------------------------------------------")

def buscar_juegos_por_plataforma_y_calificacion(plataforma, calificacion_min):
    encontrados=False

    for id, caracteristicas in juegos_catalogo.items():
        if id in inventario_tienda and inventario_tienda[id][0] > 0:
            if plataforma.lower() == caracteristicas[3].lower():
                if calificacion_min <= caracteristicas[5]:
                    print(f"{id} -> {caracteristicas}")
                    encontrados=True
    if not encontrados:
        print("No se encontraron juegos con esos criterios")

def actualizar_precio_juego(id_juego, nuevo_precio):
    
    if id_juego not in juegos_catalogo or nuevo_precio <=0:
        return False
    else:
        inventario_tienda[id_juego][1]=nuevo_precio
        return True
    
def listar_juegos_por_desarrollador(desarrollador):
    encontrado=False
    for id, caracteristicas in juegos_catalogo.items():
        if id in inventario_tienda and desarrollador.lower() == caracteristicas[1].lower():
            print(f"{id} ->{caracteristicas} Copias disponibles: {inventario_tienda[id][0]} Precio: {inventario_tienda[id][1]}")
            encontrado= True
    if not encontrado:
        print(f"No se encontraron juegos del desarrollador {desarrollador}")
            

def main():
    while True:
        menu()
        op=input("Ingresa una opcion (1/2/3/4): ")

        if op == "1":
            while True:
                plataforma=input("ingresa la plataforma para ver los juegos disponibles: ").strip().lower()
                try:
                    calificacion_min=int(input("Ingresa el puntaje mínimo de Metacritic en valores enteros: "))
                    buscar_juegos_por_plataforma_y_calificacion(plataforma, calificacion_min)
                    break
                except ValueError:
                    print("Ingresa un numero entero!")

                

        elif op == "2":
            while True:

                id_juego=input("Ingrese el id del juego para modificar su precio: ").upper()
                try:
                    nuevo_precio=int(input("Ingrese el nuevo precio: "))                
                    
                    if actualizar_precio_juego(id_juego, nuevo_precio):
                        print("Precio actualizado con éxito")
                    else:
                        print("No se pudo actualizar el precio. ID inexistente o precio inválido!!")

                except ValueError:
                    print("debe ingresar un numero entero positivo!")

                
                continuar=input("¿Desea modificar otro precio de producto? si/no: ")
                if continuar != "si":
                    break

        elif op == "3":

            desarrollador=input("Ingrese un nombre de desarrollador para buscar: ").lower().strip()
            listar_juegos_por_desarrollador(desarrollador)

        elif op == "4":
            print("Programa finalizado. ¡Gracias por usar GameVault!")
            break
        else:
            print("Ingrese una opción válida (1/2/3/4)")

main()