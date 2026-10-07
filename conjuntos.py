#crear dos conjuntos con el nombre de 5 alumnos de dos clases
grupo1 = {"alumno1","alumno2","alumno3","alumno4","alumno5"}
grupo2 = {"alumno6","alumno7","alumno8","alumno9","alumno5"}

union = grupo1 | grupo2
interseccion = grupo1 & grupo2
diferencia = grupo1 - grupo2
diferencia_simetrica = grupo1 ^ grupo2

print(f"union {union}")
print(f"interseccion {interseccion}")
print(f"diferencia {diferencia}")
print(f"diferencia_simetrica {diferencia_simetrica}")

