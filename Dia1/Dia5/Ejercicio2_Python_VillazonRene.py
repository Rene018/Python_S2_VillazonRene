def registrarEmpleado():
    nombre = input('Ingrese el nombre: ')
    while True:
        horas = int(input('Ingrese las horas trabajadas (mayor a 0): '))
        if horas > 0:
            break
    return nombre, horas


total_bruto = total_eps = total_pension = total_neto = 0
mayor_neto = menor_neto = 0
nombre_mayor = nombre_menor = ''

n = int(input('Ingrese el número de empleados: '))

for i in range(1, n + 1):
    print('----------------------------------------')
    print(f'Empleado {i}:')
    nombre, horas = registrarEmpleado()

    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    total_bruto += bruto
    total_eps += eps
    total_pension += pension
    total_neto += neto

    if neto > mayor_neto:
        mayor_neto = neto
        nombre_mayor = nombre

    if menor_neto == 0 or neto < menor_neto:
        menor_neto = neto
        nombre_menor = nombre

print('========================================')
print('ESTADÍSTICAS FINALES:')
print(f'Total Sueldos Brutos     : ${total_bruto:,.2f}')
print(f'Total Descuento EPS      : ${total_eps:,.2f}')
print(f'Total Descuento Pensión  : ${total_pension:,.2f}')
print(f'Total Sueldos Netos      : ${total_neto:,.2f}')
print(f'Promedio Sueldo Bruto    : ${total_bruto / n:,.2f}')
print(f'Promedio Sueldo Neto     : ${total_neto / n:,.2f}')
print(f'Mayor sueldo neto        : {nombre_mayor} (${mayor_neto:,.2f})')
print(f'Menor sueldo neto        : {nombre_menor} (${menor_neto:,.2f})')
print('========================================')
