cont = 1
personas = []
persona = {}
booleanito = True
while (booleanito):
    cont += 1
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    # CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario = int(input("Escoja una opción (Numérica):"))
    if (opcionUsuario == 1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        edad = int(input('edad: '))
        for i in range(2):
            telefono = {'identificador': input('identificador: '),
                        'telefono': input('telefono: '),
                        'tipo': input('tipo: ')}
            telefonos = [telefono]
            telefono = {}
        persona = {
            'id': cont,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'telefono': telefonos
        }
        personas.append(persona)
        persona = {}
        cont += 1
    elif (opcionUsuario == 2):
        print("#################")
        print("#### Lista Personas ####")
        print("#################")
        for persona in range(len(personas)):
            for atributo in personas[persona]:
                print(atributo, ': ', personas[persona][atributo])
    elif (opcionUsuario == 3):
        print("#################")
        print("#### Persona ####")
        print("#################")
        busacado = input('ingrese el nombre de la persona')
        for persona in range(len(personas)):
            if (persona["nombre"] == busacado):
                for atributo in personas[persona]:
                    print(atributo, ': ', personas[persona][atributo])

    elif (opcionUsuario == 4):
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
        busacado = input('ingrese el nombre de la persona')
        for persona in range(len(personas)):
            if (persona["nombre"] == busacado):
                nombre = input('nombre: ')
                apellido = input('apellido: ')
                edad = int(input('edad: '))
                for i in range(2):
                    print('telefono ', i+1)
                    telefono = {'identificador': input('identificador: '),
                                'telefono': input('telefono: '),
                                'tipo': input('tipo: ')}
                    telefonos = [telefono]
                    telefono = {}
                persona = {
                    'id': cont,
                    'nombre': nombre,
                    'apellido': apellido,
                    'edad': edad,
                    'telefono': telefonos
                }
    elif (opcionUsuario == 5):
        print("#################")
        print("#### Borrar Persona ####")
        print("#################")
        busacado = input('ingrese el nombre de la persona')
        for persona in range(len(personas)):
            if (persona["nombre"] == busacado):
                personas.remove(persona)
    elif (opcionUsuario == 6):
        booleanito = False
    else:
        print("No es una opción válida")
