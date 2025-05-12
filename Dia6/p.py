myObj={
    'nombre':'holi',
    'edad':12
}
lista=[myObj,myObj]
'''
for i in range(2):
    n=input('nombre')
    e=int(input('edad'))
    myObj['nombre']=n
    myObj['edad']=e
    lista.append(myObj)
    myObj={}




    '''
for i in range(len(lista)):
    print(lista[i])
    for n in lista[i]:
        print(n)
        print(lista[i][n])