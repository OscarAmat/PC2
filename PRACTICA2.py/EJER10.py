def obtener_fecha():
    
    ingresar_fecha = input("Ingrese la fecha (mes-día-año): ")

    try:
        
        mes, dia, anio = map(int, ingresar_fecha.split('/'))

       
        fecha_esperada = f"{anio:04d}-{mes:02d}-{dia:02d}"
        return fecha_esperada
    except ValueError:
        print("Formato de fecha no válido.")
        return None


fecha_esperada = obtener_fecha()
if fecha_esperada:
    print({fecha_esperada})