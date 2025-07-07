
def mostrar_menu():
    print("\n--- SISTEMA DE GESTION DE CALIFICACIONES ---")
    print()
    print("1. Añadir nuevo estudiante")
    print("2. Registrar/Actualizar calificación de estudiante")
    print("3. Ver calificaciones de un estudiante")
    print("4. Ver resumen de calificaciones de todos los estudiantes")
    print("5.- Salir.")
    print("---------------------------------------------------------")

def add_estudiante(calificaciones_estudiantes):
    while True:
        nombre=input("Ingrese el nombre del estudiante: ").strip()
        if not nombre:
            print("Debe ingresar un nombre válido")
            continue
        elif nombre in calificaciones_estudiantes:
            print("El nombre ya está registrado")
            continue
        else:
            break
    print("Estudiante agregado con éxito")
    calificaciones_estudiantes[nombre]={
    }    

def actualizar_nota(calificaciones_estudiantes):

    while True:
        nom_actualizar_nota=input("Ingrese el nombre del estudiante que desea actualizar: ")
        if nom_actualizar_nota not in calificaciones_estudiantes:
            print("El nombre no está registrado, debe ir a registrarlo primero")
            return
        else:
            break
    while True:

        nombre_asignatura=input("Ingrese el nombre de la asignatura: ")
        if not nombre_asignatura:
            print("El nombre de la asignatura no puede estar vacío.")
            continue
        else:
            break

    while True:

        try:
            calificacion=float(input("Ingrese la calificación: "))
        except ValueError:
            print("Debe ingresar un valor numérico")
            continue

        if 1.0 <= calificacion <= 7.0:
            calificaciones_estudiantes[nom_actualizar_nota][nombre_asignatura]=calificacion
            print("Calificación agregada con éxito")
            break
            
        else:
            print("Debe ingresar una nota entre 1.0 y 7.0")
            continue
        

def ver_calificacion(calificaciones_estudiantes):

    while True:
        nom_ver=input("Ingrese el nombre del estudiante para ver sus calificaciones: ")
        if nom_ver not in calificaciones_estudiantes:
            print("El Estudiante no está registrado, debe registrarlo primero")
            return
        else:
            break
    
    asignaturas_notas=calificaciones_estudiantes[nom_ver]
    for asignatura, nota in asignaturas_notas.items():
        print(f"{asignatura}:{nota}")


def ver_calificaciones(calificaciones_estudiantes):

    for alumnos, notas in calificaciones_estudiantes.items():
        print(f"alumno: {alumnos}, notas: {notas}")
        
    return


def main():

    calificaciones_estudiantes = {
        "Ana Garcia": {
            "Matematicas": 6.5,
            "Historia": 5.8
        },
        "Luis Perez": {
            "Ciencias": 6.0,
            "Lenguaje": 7.0
        }
    }

    while True:
        mostrar_menu()
        try:
            op=int(input("Ingrese una opcion valida del 1 al 5: "))

            if op in [1,2,3,4,5]:

                if op == 1: 
                    add_estudiante(calificaciones_estudiantes)
                elif op == 2:
                    actualizar_nota(calificaciones_estudiantes)
                elif op == 3:
                    ver_calificacion(calificaciones_estudiantes)
                elif op == 4:
                    ver_calificaciones(calificaciones_estudiantes)
                elif op == 5:
                    print("Hasta luego!!")
                    break
            else:
                print("ingrese una opción válida")
        
        except ValueError:
            print("Ingrese un valor numérico")

main()
