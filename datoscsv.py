import csv

grupo1 = set()
grupo2 = set()

with open("alumnosgrupo1.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        grupo1.add(fila[0])

with open("alumnosgrupo2.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        grupo2.add(fila[0])

union = grupo1 | grupo2
interseccion = grupo1 & grupo2
diferencia = grupo1 - grupo2
diferencia_simetrica = grupo1 ^ grupo2

print(f"union {union}")
print(f"interseccion {interseccion}")
print(f"diferencia {diferencia}")
print(f"diferencia_simetrica {diferencia_simetrica}")