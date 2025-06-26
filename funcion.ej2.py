
def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multi(a, b):
    return a*b

def divi(a, b):
    if b ==0:
        return "error"
    else:
        return a/b

def validar_numero(numero_entrada):
    try:
        while True:
            numero=float(input(numero_entrada))
            return numero
    except ValueError:
        print("ingrese un caracter numérico válido")


num1=validar_numero("ingrese el primer numero: ")
num2=validar_numero("ingrese el segundo numero: ")

resultado_suma=suma(num1, num2)
resultado_resta=resta(num1, num2)
resultado_multi=multi(num1,num2)
resultado_divi=divi(num1,num2)

print(f"el resumtado de la suma es: {resultado_suma}. EL resultado de la resta es: {resultado_resta}")
print(f"el resultado de la multiplicacion es: {resultado_multi} y el resultado de la division es: {resultado_divi}")
