def seleccionarOpcion(mensaje, opcion1Texto, precio1, opcion2Texto, precio2):
    opcion = 0
    while opcion != 1 and opcion != 2:
        print('Seleccione', mensaje)
        print('1.', opcion1Texto)
        print('2.', opcion2Texto)
        try:
            opcion = int(input('Ingrese opción (1 o 2): '))
        except ValueError:
            pass
    if opcion == 1:
        precio = precio1
    else:
        precio = precio2
    return precio


def seleccionarBebida(mensaje, opcion1Texto, precio1, opcion2Texto, precio2, opcion3Texto, precio3):
    opcion = 0
    while opcion < 1 or opcion > 3:
        print('Seleccione', mensaje)
        print('1.', opcion1Texto)
        print('2.', opcion2Texto)
        print('3.', opcion3Texto)
        try:
            opcion = int(input('Ingrese opción (1, 2 o 3): '))
        except ValueError:
            pass
    if opcion == 1:
        precio = precio1
    elif opcion == 2:
        precio = precio2
    else:
        precio = precio3
    return precio


total = 0
while True:
    n = int(input('Número de hamburguesas a ordenar: '))
    if n > 0:
        break

for i in range(n):
    print('--- Hamburguesa Número', i + 1, '---')
    precioHamburguesa = 0
    precioHamburguesa += seleccionarOpcion(
        'el tipo de pan:', 'Centeno $1000', 1000, 'Avena $1500', 1500)
    precioHamburguesa += seleccionarOpcion(
        'la carne:', '250g $5000', 5000, '300g $7000', 7000)
    precioHamburguesa += seleccionarOpcion(
        'el pollo:', '250g $4500', 4500, '350g $5500', 5500)
    precioHamburguesa += seleccionarOpcion(
        'el pollo desmechado:', '250g $6500', 6500, '350g $7500', 7500)
    precioHamburguesa += seleccionarOpcion(
        'la tocineta:', '1 lonja $1500', 1500, '2 lonjas $2500', 2500)
    precioHamburguesa += seleccionarOpcion(
        'el tipo de papa:', 'A la francesa $5000', 5000, 'En cascos $6000', 6000)
    precioHamburguesa += seleccionarBebida('la bebida:', 'Gaseosa $5000',
                                           5000, 'Cerveza Club Colombia $8000', 8000, 'Naranjada $9000', 9000)
    total += precioHamburguesa

servicio = total * 0.10
totalFinal = total + servicio

print('--------------------------------')
print('Subtotal sin servicio: $', total)
print('Servicio 10%: $', servicio)
print('TOTAL A PAGAR: $', totalFinal)
