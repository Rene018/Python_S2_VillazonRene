total = 0

while True:
    n = int(input("Número de hamburguesas a ordenar: "))
    if n > 0:
        break

for i in range(n):
    print(f"--- Hamburguesa Número {i + 1} ---")
    precioHamburguesa = 0

    while True:
        print("Seleccione el tipo de pan:\n 1. Centeno $1000\n 2. Avena $1500")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 1000
            break
        elif opcion == 2:
            precioHamburguesa += 1500
            break

    while True:
        print("Seleccione la carne:\n 1. 250g $5000\n 2. 300g $7000")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 5000
            break
        elif opcion == 2:
            precioHamburguesa += 7000
            break

    while True:
        print("Seleccione el pollo:\n 1. 250g $4500\n 2. 350g $5500")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 4500
            break
        elif opcion == 2:
            precioHamburguesa += 5500
            break

    while True:
        print("Seleccione el pollo desmechado:\n 1. 250g $6500\n 2. 350g $7500")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 6500
            break
        elif opcion == 2:
            precioHamburguesa += 7500
            break

    while True:
        print("Seleccione la tocineta:\n 1. 1 lonja $1500\n 2. 2 lonjas $2500")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 1500
            break
        elif opcion == 2:
            precioHamburguesa += 2500
            break

    while True:
        print("Seleccione el tipo de papa:\n 1. A la francesa $5000\n 2. En cascos $6000")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 5000
            break
        elif opcion == 2:
            precioHamburguesa += 6000
            break

    while True:
        print("Seleccione la bebida:\n 1. Gaseosa $5000\n 2. Cerveza Club Colombia $8000\n 3. Naranjada $9000")
        opcion = int(input())
        if opcion == 1:
            precioHamburguesa += 5000
            break
        elif opcion == 2:
            precioHamburguesa += 8000
            break
        elif opcion == 3:
            precioHamburguesa += 9000
            break

    total += precioHamburguesa

servicio = total * 0.10
totalFinal = total + servicio

print('--------------------------------')
print(f'Subtotal sin servicio: ${total}')
print(f'Servicio 10%: ${servicio}')
print(f'TOTAL A PAGAR: ${totalFinal}')
