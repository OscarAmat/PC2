def cantidad_digito(numero, digito):
    cantidad = str(numero).count(str(digito))
    
   
    print(f"Número ingresado: {numero} y Dígito: {digito}")
    print(f"Cantidad de veces {digito} en el número: {cantidad}")

cantidad_digito(6633005574197235,5)

#INGRESAR DENTRO DE LA FUNCION cantidad_digito, EL NUMERO y DIGITO