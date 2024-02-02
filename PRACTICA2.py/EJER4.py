n = int(input("Ingrese el número de alumnos: "))

estudiantes = [{"Alumno": input("Ingrese el nombre del alumno: "),
                  "Notas": [int(input(f"Ingrese la nota {i + 1}: ")) for i in range(3)]}
                 for _ in range(n)]

print("\nListado de Alumnos:")
for alumno in estudiantes:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
