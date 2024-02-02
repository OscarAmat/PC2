import math 

def factorial(numero):

    if numero < 0:
        return "no es factorial"
    else:
        return math.factorial(numero)

ingresar_numero = 10
#INGRESAR CUALQUIER NUMERO POSITIVO
resultado = factorial(ingresar_numero)
print(f"El factorial es: {resultado}")