opc= int(input('elija la operacion que desea realizar:\n 1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Dividir')
)
num1=float(input('ingrese el primer numero'))
num2=float(input('ingrese el segundo numero'))
if opc==1:
    print(f'{num1}+{num2}= {num1+num2}')
elif opc==2:
    print(f'{num1}-{num2}= {num1-num2}')
elif opc==3:
    print(f'{num1}x{num2}= {num1*num2}')
elif opc==4:
    print(f'{num1}/{num2}= {num1/num2}')