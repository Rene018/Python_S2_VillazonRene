
# Verificar si un número es primo
numero = 17
es_primo = True
if numero < 2:
    esPrimo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        print(int(numero**0.5)+1)
        if numero % i == 0:
            es_primo = False
            break
print('Es primo:', esPrimo)
