cont = 1
personas = [{
  "id": 1,
  "nombre": "Carlos",
  "apellido": "Gómez",
  "edad": 30,
  "telefono": [
    {
      "identificador": "personal",
      "telefono": "3111234567",
      "tipo": "móvil"
    },
    {
      "identificador": "trabajo",
      "telefono": "6041234567",
      "tipo": "fijo"
    }
  ]
},{
  "id": 2,
  "nombre": "Laura",
  "apellido": "Martínez",
  "edad": 25,
  "telefono": [
    {
      "identificador": "casa",
      "telefono": "6017654321",
      "tipo": "fijo"
    },
    {
      "identificador": "emergencia",
      "telefono": "3209876543",
      "tipo": "móvil"
    }
  ]
}]
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
            print('################################')
            for atributo in personas[persona]:
                if atributo!='telefono':
                    print(atributo, ': ', personas[persona][atributo])
                else:
                    for telefono in personas[persona][atributo]:
                        for atri in telefono:                       
                            print(atri, ': ', telefono[atri])
                        
                      
    elif (opcionUsuario == 3):
        print("#################")
        print("#### Persona ####")
        print("#################")
        busacado = input('ingrese el nombre de la persona')
        for persona in range(len(personas)):
            if (persona["id"] == busacado):
                for atributo in personas[persona]:
                    if atributo!='telefono':
                        print(atributo, ': ', personas[persona][atributo])
                    else:
                        for telefono in personas[persona][atributo]:
                            for atri in telefono:                       
                                print(atri, ': ', telefono[atri])

    elif (opcionUsuario == 4):
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
        busacado = input('ingrese el nombre de la persona')
        for persona in range(len(personas)):
            if (persona["id"] == busacado):
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
            if (persona["id"] == busacado):
                personas.remove(persona)
    elif (opcionUsuario == 6):
        booleanito = False
    else:
        print("No es una opción válida")
