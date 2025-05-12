
personas=[]
persona={}
booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        nombre=input('nombre')
        apellido=input('apellido')
        edad=int(input('edad'))
        
        personas.append()
    elif(opcionUsuario==2):
        print("#################")
        print("#### Lista Personas ####")
        print("#################")
    elif(opcionUsuario==3):
        print("#################")
        print("#### Persona ####")
        print("#################")
    elif(opcionUsuario==4):
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
    elif(opcionUsuario==5):
        print("#################")
        print("#### Borrar Persona ####")
        print("#################")
    elif(opcionUsuario==6):
        booleanito=False
    else:
        print("No es una opción válida")