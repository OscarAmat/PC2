datos = []

while True:
    ingresar_numero = input("¿Desea ingresar un número?: ")
    
    if ingresar_numero.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        datos.append(numero)
    elif ingresar_numero.upper() == "NO":
        break
    else:
        print("error")
print("Numeros ingresados", datos)
numeros_par= sum(1 for num in datos if num % 2 == 0)
numeros_impares = len(datos) - numeros_par

print("Cantidad de numeros par: ",numeros_par )
print("Cantidad de numeros impar: ",numeros_impares )