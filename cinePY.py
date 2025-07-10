# catalogo_peliculas = {ID_pelicula: [Título, Director, Género, Año, Duración_min, 
# Calificación_IMDb], ...]

catalogo_peliculas = {
    'P001': ['El Viaje de Chihiro', 'Hayao Miyazaki', 'Animación', 2001, 125, 8.6],
    'P002': ['Pulp Fiction', 'Quentin Tarantino', 'Crimen', 1994, 154, 8.9],
    'P003': ['Origen', 'Christopher Nolan', 'Ciencia Ficción', 2010, 148, 8.8],
    'P004': ['Parasitos', 'Bong Joon-ho', 'Drama', 2019, 132, 8.5],
    'P005': ['Interstellar', 'Christopher Nolan', 'Ciencia Ficción', 2014, 169, 8.6],
    'P006': ['La La Land', 'Damien Chazelle', 'Musical', 2016, 128, 8.0],
    'P007': ['El Padrino', 'Francis Ford Coppola', 'Crimen', 1972, 175, 9.2],
    'P008': ['Spider-Man: Un Nuevo Universo', 'Bob Persichetti', 'Animación', 2018, 117, 8.4],
    'P009': ['Matrix', 'Lana Wachowski', 'Ciencia Ficción', 1999, 136, 8.7],
    }
 
# stock_alquiler = {ID_pelicula: [copias_disponibles, precio_alquiler_por_dia], ...]
stock_alquiler = {

    'P001': [5, 2500],
    'P002': [3, 3000],
    'P003': [7, 2800],
    'P004': [2, 3500],
    'P005': [0, 2800],  # Película sin copias disponibles
    'P006': [10, 2000],
    'P007': [1, 4000],
    'P008': [8, 2200],
    'P009': [4, 2700],
    }

def mostrar_menu():
    print("--------------------------------------")
    print("\n--- MENÚ PRINCIPAL ---")
    print("--------------------------------------")
    print("1. Buscar películas por Género y Año")
    print("2. Actualizar copias disponibles")
    print("3. Listar películas por Director")
    print("4.- Salir.")
    print("--------------------------------------")

def buscar_pelis_genero_age(genero, age_min, age_max):
    pelis_encontradas= False

    for id, datos in catalogo_peliculas.items():
        if id in stock_alquiler and stock_alquiler[id][0] >0:
            genero_buscar=datos[2].lower()
            age_peli=datos[3]
            if genero_buscar == genero.lower() and age_min <= age_peli <= age_max:
                print(f"Genero: {genero} -> {datos}")
                pelis_encontradas=True

    if not pelis_encontradas:
        print("No existen peliculas disponibles para los datos ingresados")

def actualizar_copias(id_pelicula, nuevas_copias):
    global stock_alquiler

    if id_pelicula in catalogo_peliculas and id_pelicula in stock_alquiler\
    and nuevas_copias >= 0:
        stock_alquiler[id_pelicula][0]=nuevas_copias
        print("copias actualizadas con éxito!")
        return True
    else:
        print("El ID de película no existe o la cantidad es inválida!!")
        return False
    
def listar_peliculas_por_director(director):
    encontradas=False

    for id, datos in catalogo_peliculas.items():
        if id in stock_alquiler:
            if director.lower() == datos[1].lower():
                print(f"{datos}")
                encontradas=True
    
    if not encontradas:
        print(f"No se encontraron peliculas de: {director}")
    
def main():

    while True:
        mostrar_menu()

        op=input("ingrese una opcion (1/2/3/4): ")
        if op == "1":
            while True:
                genero=input("Ingrese el genero de la pelicula: ").strip().lower()
                try:
                    age_min=int(input("Ingrese el año minimo: "))
                    age_max=int(input("Ingrese el año maximo: "))
                    if age_min > age_max:
                        print("el umbral inferior de año no puede ser mayor que el superior")
                        continue
                    else:
                        buscar_pelis_genero_age(genero, age_min, age_max)
                        break
                except ValueError:
                    print("ingrese un numero entero")
                

        elif op == "2":
            while True:
                id_pelicula=input("Ingrese el id de la película: ").upper()
                try:
                    nuevas_copias=int(input("Ingrese el nuevo stock para actualizar: "))
                    actualizar_copias(id_pelicula, nuevas_copias)
                except ValueError:
                    print("ingresa un valor numérico")
                
                
                continuar=input("¿desea actualizar otro stock? (si/no): ").lower()
                if continuar != "si":
                    break
        
        elif op == "3":

            director=input("Ingrese el nombre del director: ").lower()
            listar_peliculas_por_director(director)
        
        elif op == "4":
            print("Programa finalizado. ¡Gracias por usar CinePy!")
            break

main()


            