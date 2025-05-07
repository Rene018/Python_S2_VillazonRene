def sumar(a,b):
    print(f'{a}+{b}= {a+b}')
def restar(a,b):
    print(f'{a}-{b}= {a-b}')
def multiplicar(a,b):
    print(f'{a}*{b}= {a*b}')
def dividir(a,b):
    print(f'{a}/{b}= {a/b}')

opc= input(int('elija la operacion que desea realizar:\n 1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Dividir')
)
num1=input(float('ingrese el primer numero'))
num2=input(float('ingrese el segundo numero'))
if opc==1:
    sumar(num1,num2)
elif opc==2:
    restar(num1,num2)
elif opc==3:
    multiplicar(num1,num2)
elif opc==4:
    dividir(num1,num2)