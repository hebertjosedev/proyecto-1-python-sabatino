## Elaborar un programa en consola que pueda gestionar estudiantes universitarios, a continuacion se presentan los requerimientos:
"""
1. El programa debe tener un menu con las siguientes secciones:
    * 1- listado de estudiantes
    * 2- registrar estudiantes
    * 3- actualizar estudiante
    * 4- eliminar estudiante
    * 5- salir
"""

estudiantes = []

while True:
    print("Bienvenido al sistema interno de la universidad ASTRO")
    print("Menu:")
    print("1: Matricula estudiantil")
    print("2: Registrar")
    print("3: Actualizar")
    print("4: Eliminar")
    print("5: Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print(50* '-', 'ASTRO', 50* '-')
        total_estudiantes = len(estudiantes)
        print('Total de estudiantes: ',total_estudiantes)
        if estudiantes != []:
           for estudiante in estudiantes:
              print(120 * '-')
              print('Nombre:',estudiante['nombre'],'|','Apellido:',estudiante['apellido'],'|','Cedula: ',estudiante['cedula'],'|','nota1: ', estudiante['nota1'],'|','Nota2: ', estudiante['nota2'],'|','nota3: ', estudiante['nota3'],'|','promedio: ', "%.f" % ((int(estudiante['nota1'])+int(estudiante['nota2'])+int(estudiante['nota3']))/3)   )
              print(120 * '-') 

        else: 
           print("No hay estudiantes, animate a ser el primero en registrarte")
           print(50* '-', 'ASTRO', 50* '-')

    elif opcion == 2:
        nombre = ''
        apellido = ''
        cedula = 0
        nota1 = 0
        nota2 = 0
        nota3 = 0
        print("Ingresa los siguientes datos para registrarte en matricula")
        nombre_estudiante = input("Ingresa tu nombre: ")
        is_boolean = True

        while is_boolean:
            is_name = nombre_estudiante.isalpha()
            if is_name == True:
             nombre = nombre_estudiante.capitalize()
             break
            elif is_name == False: 
                print("Nombre invalido, debes ingresar solo letras")
                nombre_estudiante_error = input("Ingresa un nombre correcto: ")
                is_boolean2 = nombre_estudiante_error.isalpha()
                if is_boolean2 == True:
                    is_boolean = False
                    nombre = nombre_estudiante_error.capitalize()
                    break

        apellido_estudiante = input("Ingresa tu apellido: ")
        is_boolean = True

        while is_boolean:
            is_apellido = apellido_estudiante.isalpha()
            if is_apellido == True:
             apellido = apellido_estudiante.capitalize()
             break
            elif is_apellido == False: 
                print("apellido invalido, debes ingresar solo letras")
                apellido_estudiante_error = input("Ingresa un apellido correcto: ")
                is_boolean2 = apellido_estudiante_error.isalpha()
                if is_boolean2 == True:
                    apellido = apellido_estudiante_error.capitalize()
                    is_boolean = False

        cedula_estudiante = input("Ingresa tu cedula: ")
        is_boolean = True

        while is_boolean:
            is_cedula = cedula_estudiante.isdigit()
            if is_cedula == True:
             cedula = int(cedula_estudiante)
             break
            elif is_cedula == False: 
                print("cedula invalido, debes ingresar solo numeros")
                cedula_estudiante_error = input("Ingresa un cedula correcto: ")
                is_boolean2 = cedula_estudiante_error.isdigit()
                if is_boolean2 == True:
                    cedula = int(cedula_estudiante_error)
                    is_boolean = False

        nota1_estudiante = input("Ingresa tu nota1: ")
        is_boolean = True

        while is_boolean:
            is_nota1 = nota1_estudiante.isdigit()
            if is_nota1 == True:
             nota1 = nota1_estudiante
             break
            elif is_nota1 == False: 
                print("nota1 invalido, debes ingresar solo numeros")
                nota1_estudiante_error = input("Ingresa un nota1 correcto: ")
                is_boolean2 = nota1_estudiante_error.isdigit()
                if is_boolean2 == True:
                    nota1 = int(nota1_estudiante_error)
                    is_boolean = False

        nota2_estudiante = input("Ingresa tu nota2: ")
        is_boolean = True

        while is_boolean:
            is_nota2 = nota2_estudiante.isdigit()
            if is_nota2 == True:
             nota2 = nota2_estudiante
             break
            elif is_nota2 == False: 
                print("nota2 invalido, debes ingresar solo numeros")
                nota2_estudiante_error = input("Ingresa un nota2 correcto: ")
                is_boolean2 = nota2_estudiante_error.isdigit()
                if is_boolean2 == True:
                    nota2 = int(nota2_estudiante_error)
                    is_boolean = False

        nota3_estudiante = input("Ingresa tu nota3: ")
        is_boolean = True

        while is_boolean:
            is_nota3 = nota3_estudiante.isdigit()
            if is_nota3 == True:
             nota3 = nota3_estudiante
             break               

            elif is_nota3 == False: 
                print("nota3 invalido, debes ingresar solo numeros")
                nota3_estudiante_error = input("Ingresa un nota3 correcto: ")
                is_boolean2 = nota3_estudiante_error.isdigit()
                if is_boolean2 == True:
                    nota3 = int(nota3_estudiante_error)
                    is_boolean = False

        diccionario_modelo = {}
        diccionario_modelo['nombre']=f'{nombre}'
        diccionario_modelo['apellido']=f'{apellido}'
        diccionario_modelo['cedula']=f'{cedula}'
        diccionario_modelo['nota1']=f'{nota1}'
        diccionario_modelo['nota2']=f'{nota2}'
        diccionario_modelo['nota3']=f'{nota3}'
        diccionario_modelo['promedio']= f'{"%.f" % ((int(nota1)+int(nota2)+int(nota3))/3)}'
        estudiantes.append(diccionario_modelo)
        print("Te has registrado con exito!")

    
    elif opcion == 3:
        cedula_estudiante_actualizacion = input("Ingresa tu cedula para actualizar datos: ")
        boolean = False
        estudiantes_copia = estudiantes.copy()
        for cedulas in estudiantes_copia:
                if cedulas['cedula'] == cedula_estudiante_actualizacion:
                  boolean = True
                  while boolean:
                    print(f"Hola, {cedulas['nombre']} elige tu opcion a actualizar:")
                    print("1: Nombre")
                    print("2: Apellido")
                    print("3: Cedula")
                    print("4: Nota1")
                    print("5: Nota2")
                    print("6: Nota3")

                    dato_actualizar = int(input("Selecciona tu numero de opcion a actualizar : "))
                    
                    if dato_actualizar == 1:
                        nombre_nuevo = input("Ingresa tu nombre correctamente: ") 
                        if nombre_nuevo.isalpha():
                         cedulas['nombre'] = nombre_nuevo.capitalize()
                         print(f"ACTUALIZASTE TU NOMBRE, EXITOSAMENTE!")
                         break
                        else: print("El nombre es invalido, ingresa nuevamente un nombre correctamente")

                    elif dato_actualizar == 2:
                        apellido_nuevo = input("Ingresa tu apellido correctamente: ")
                        if apellido_nuevo.isalpha(): 
                         cedulas['apellido'] = apellido_nuevo.capitalize()
                         print(f"ACTUALIZASTE TU APELLIDO, EXITOSAMENTE!")
                         break
                        else: print("El apellido es invalido, ingresa nuevamente un apellido correcto")


                    elif dato_actualizar == 3:
                        cedula_nueva = input("Ingresa tu cedula correctamente: ") 
                        if cedula_nueva.isdigit():
                         cedulas['cedula'] = cedula_nueva
                         print(f"ACTUALIZASTE TU CEDULA, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, solo numeros con puntos para la cedula")

                    elif dato_actualizar == 4:
                        nota1_nuevo = input("Ingresa tu nota1 correctamente: ") 
                        if nota1_nuevo.isdigit():
                         cedulas['nota1'] = nota1_nuevo
                         print(f"ACTUALIZASTE TU NOTA1, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, ingresa numeros solamente")
                    
                    elif dato_actualizar == 5:
                        nota2_nuevo = input("Ingresa tu nota2 correctamente: ") 
                        if nota2_nuevo.isdigit():
                         cedulas['nota2'] = nota2_nuevo
                         print(f"ACTUALIZASTE TU NOTA2, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, ingresa solo numeros")

                    elif dato_actualizar == 6:
                        nota3_nuevo = input("Ingresa tu nota3 correctamente: ") 
                        if nota3_nuevo.isdigit():
                         cedulas['nota3'] = nota3_nuevo
                         print(f"ACTUALIZASTE TU NOTA3, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, ingresa solo numeros")

        if boolean == False:
           print(f"Dato invalido : {cedula_estudiante_actualizacion} no apareces en nuestro sistema, registrate en la opcion 4")
        
    
                

    elif opcion == 4:
        print("Ingresa tu numero de cedula para confirmar la eliminacion en matricula")
        cedula_ingresada = input("Solo numeros: ")
        i = 0
        estudiantes_copia = estudiantes.copy()
        for cedulas in estudiantes_copia:
            if cedulas['cedula'] == cedula_ingresada:
                        del estudiantes[i]
                        print(f"Estudiante {cedulas['nombre']} sus datos han sido eliminados con exito!")
                        break

            elif cedulas != cedula_ingresada:
                i += 1
                
        else: print("No tenemos tu cedula en nuestro sistema")
                
        

    elif opcion == 5:
        print("Hasta pronto buen estudiante!")
        break

    else: print("Elige una opcion valida")