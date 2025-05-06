totalBruto = totalEPS = totalPension = totalNeto = 0
mayorNeto = 0
menorNeto = 0
nombreMayor = nombreMenor = ""

n = int(input("Ingrese el número de empleados: "))

for i in range(1, n + 1):
    print("----------------------------------------")
    print(f"Empleado {i}:")
    nombre = input("Ingrese el nombre: ")

    while True:
        horas = int(input("Ingrese las horas trabajadas (mayor a 0): "))
        if horas > 0:
            break

    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    totalBruto += bruto
    totalEPS += eps
    totalPension += pension
    totalNeto += neto

    if neto > mayorNeto:
        mayorNeto = neto
        nombreMayor = nombre

    if menorNeto == 0 or neto < menorNeto:
        menorNeto = neto
        nombreMenor = nombre

print("========================================")
print("ESTADÍSTICAS FINALES:")
print(f"Total Sueldos Brutos: ${totalBruto}")
print(f"Total Descuento EPS: ${totalEPS}")
print(f"Total Descuento Pensión: ${totalPension}")
print(f"Total Sueldos Netos: ${totalNeto}")
print(f"Promedio Sueldo Bruto: ${totalBruto / n}")
print(f"Promedio Sueldo Neto: ${totalNeto / n}")
print(f"Empleado con mayor sueldo neto: {nombreMayor} (${mayorNeto})")
print(f"Empleado con menor sueldo neto: {nombreMenor} (${menorNeto})")
print("========================================")
