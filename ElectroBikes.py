import time

# bicicletas = {codigo: [marca, autonomía_km, batería_Wh, color, suspensión, garantía_meses], ...}
bicicletas = {
    'EB100': ['Xiaomi', 50, 250, 'negro', 'delantera', 24],
    'EB200': ['Trek', 70, 400, 'rojo', 'doble', 36],
    'EB300': ['Specialized', 90, 500, 'azul', 'trasera', 24],
    'EB150': ['Xiaomi', 60, 300, 'blanco', 'ninguna', 18]
}

# stock = {codigo: [precio, cantidad], ...}
stock = {
    'EB100': [499990, 5],
    'EB200': [899990, 2],
    'EB300': [1199990, 0],  # Sin stock
    'EB150': [559990, 4]
}

def menu():
    print()
    print("*** MENÚ ELECTROBIKE ***")
    print("1. Ver stock por marca")
    print("2. Buscar por autonomía mínima y batería mínima")
    print("3. Eliminar una bicicleta")
    print("4. Salir")
    print()

def stock_marca(marca):
    stock_total=0
    encontradas=False

    for modelo, caracteristicas in bicicletas.items():
        if modelo in stock and marca.lower() == caracteristicas[0].lower():
            if stock[modelo][1] > 0:
                stock_total+=stock[modelo][1]
                encontradas=True
    if encontradas:
        print(f"Para la marca {marca} el stock es: {stock_total} unidades")
    else:
        print("No se encuentran bicicletas para la marca ingresada")
    time.sleep(2)

def buscar_autonomia_bateria(aut_min, bat_min):
    encontradas= False

    for modelo, caracteristicas in bicicletas.items():
        if modelo in stock and stock[modelo][1] >0:
            if caracteristicas[1] >= aut_min and caracteristicas[2] >= bat_min:
                print(f"{modelo} -> {caracteristicas} Precio: {stock[modelo][0]} CLP")
                encontradas=True
              
    if not encontradas:
        print("Ningún modelo ha sido encontrado para esos parámetros")
    
    time.sleep(2)
def eliminar_bicicleta(codigo):
    if codigo in bicicletas and codigo in stock:
        del bicicletas[codigo]
        del stock[codigo]
        return True
    else:
        return False
    
def main():
    while True:
        menu()

        op=input("ingrese una opcion (1/2/3/4): ")

        if op == "1":
            marca=input("Ingrese una marca: ").strip().lower()
            stock_marca(marca)

        elif op == "2":
            while True:
                try:
                    aut_min=int(input("Ingrese la autonomia mínima deseada: "))
                    bat_min=int(input("Ingrese la batería mínima deseada: "))
                    if aut_min > 0 and bat_min >0:
                        buscar_autonomia_bateria(aut_min, bat_min)
                        break
                    else:
                        print("los valores ingresados deben ser superiores a 0")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Debe ingresar un valor numérico")
                    time.sleep(2)

        elif op == "3":
            while True:
                codigo=input("Ingrese el codigo del producto que desea eliminar: ").upper()

                if eliminar_bicicleta(codigo):
                    print("Bicicleta eliminada!!")
                else:
                    print("El modelo no existe!!")
                time.sleep(2)
                continuar= input("¿desea eliminar otra bicicleta? si/no: ").lower()
                if continuar != "si":
                    break
        
        elif op == "4":
            print("Programa finalizado")
            break
        
        else:
            print("Debe ingresar una opción válida (1/2/3/4)")
            time.sleep(1)
            continue

main()