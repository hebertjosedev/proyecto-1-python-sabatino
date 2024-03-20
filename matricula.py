## Elaborar un programa en consola que pueda gestionar estudiantes universitarios, a continuacion se presentan los requerimientos:
"""
1. El programa debe tener un menu con las siguientes secciones:
    * 1- listado de estudiantes
    * 2- registrar estudiantes
    * 3- actualizar estudiante
    * 4- eliminar estudiante
    * 5- salir
"""

estudiantes = [
    {'nombre': 'mauricio', 'apellido': 'sanchez', 'cedula': '16.825.263', 'nota1':'15', 'nota2': '17', 'nota3':'19', 'promedio': '17'},
    {'nombre': 'marlon', 'apellido': 'valencia', 'cedula': '19.725.112', 'nota1':'20', 'nota2': '19', 'nota3':'10', 'promedio': '16'},
    {'nombre': 'maria', 'apellido': 'Romero', 'cedula': '12.335.243', 'nota1':'13', 'nota2': '12', 'nota3':'11', 'promedio': '12'},
    {'nombre': 'alejandra', 'apellido': 'leon', 'cedula': '27.025.263', 'nota1':'12', 'nota2': '20', 'nota3':'15', 'promedio': '16'},
    {'nombre': 'nerio', 'apellido': 'rojas', 'cedula': '25.725.339', 'nota1':'14', 'nota2': '19', 'nota3':'20', 'promedio': '18'}
]

while True:
    print("Menu:")
    print("1: Matricula estudiantil")
    print("2: Registrar")
    print("3: Actualizar")
    print("4: Eliminar")
    print("5: Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print(estudiantes)

    elif opcion == 2:
        print("Para registrarte necesitamos los siguientes datos: nombre, apellido, cedula, nota1, nota2, nota3")
        datos_estudiante_nuevo = input("Ingresa los datos en el orden solicitado: ")
        datos_separados = datos_estudiante_nuevo.split()
        longitud_cadena = len(datos_separados)

        if longitud_cadena == 6:
            nombre = datos_separados[0].isalpha()
            apellido = datos_separados[1].isalpha()
            nota1 = datos_separados[3].isdigit()
            nota2 = datos_separados[4].isdigit()
            nota3 = datos_separados[5].isdigit()
            while True:
                     if nombre == False:
                          print("Ingresa un nombre valido, sin espacios y solamente letras")
                          break
                     elif apellido == False:
                          print("Ingresa un apellido valido, sin espacios y solamente letras")
                          break
                     
                     elif nota1 == False:
                          print("las notas deben ser en numeros, ingresa correctamente tu nota 1")
                          break
                     
                     elif nota2 == False:
                          print("las notas deben ser en numeros, ingresa correctamente tu nota 2")
                          break
                     elif nota3 == False:
                          print("las notas deben ser en numeros, ingresa correctamente tu nota 3")
                          break
                     diccionario_modelo = {}
                     diccionario_modelo['nombre']=f'{datos_separados[0]}'
                     diccionario_modelo['apellido']=f'{datos_separados[1]}'
                     diccionario_modelo['cedula']=f'{datos_separados[2]}'
                     diccionario_modelo['nota1']=f'{datos_separados[3]}'
                     diccionario_modelo['nota2']=f'{datos_separados[4]}'
                     diccionario_modelo['nota3']=f'{datos_separados[5]}'
                     diccionario_modelo['promedio']= f'{"%.f" % ((int(datos_separados[3])+int(datos_separados[4])+int(datos_separados[5]))/3)}'
                     estudiantes.append(diccionario_modelo)
                     print("Te has registrado con exito!")
                     break
                          
        else: print("Te faltan datos, solo debes ingresar la cantidad de datos solicitada, ni mas ni menos") 

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
                         cedulas['nombre'] = nombre_nuevo
                         estudiantes.append(cedulas)
                         print(f"ACTUALIZASTE TU NOMBRE, EXITOSAMENTE!")
                         break
                        else: print("El nombre es invalido, ingresa nuevamente un nombre correctamente")

                    elif dato_actualizar == 2:
                        apellido_nuevo = input("Ingresa tu apellido correctamente: ")
                        if apellido_nuevo.isalpha(): 
                         cedulas['apellido'] = apellido_nuevo
                         estudiantes.append(cedulas)
                         print(f"ACTUALIZASTE TU APELLIDO, EXITOSAMENTE!")
                         break
                        else: print("El apellido es invalido, ingresa nuevamente un apellido correcto")


                    elif dato_actualizar == 3:
                        cedula_nueva = input("Ingresa tu cedula correctamente: ") 
                        if cedula_nueva.isalpha():
                         cedulas['cedula'] = cedula_nueva
                         estudiantes.append(cedulas)
                         print(f"ACTUALIZASTE TU CEDULA, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, solo numeros con puntos para la cedula")

                    elif dato_actualizar == 4:
                        nota1_nuevo = input("Ingresa tu nota1 correctamente: ") 
                        if nota1_nuevo.isdigit():
                         cedulas['nota1'] = nota1_nuevo
                         estudiantes.append(cedulas)
                         print(f"ACTUALIZASTE TU NOTA1, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, ingresa numeros solamente")
                    
                    elif dato_actualizar == 5:
                        nota2_nuevo = input("Ingresa tu nota2 correctamente: ") 
                        if nota2_nuevo.isdigit():
                         cedulas['nota2'] = nota2_nuevo
                         estudiantes.append(cedulas)
                         print(f"ACTUALIZASTE TU NOTA2, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, ingresa solo numeros")

                    elif dato_actualizar == 6:
                        nota3_nuevo = input("Ingresa tu nota3 correctamente: ") 
                        if nota3_nuevo.isdigit():
                         cedulas['nota3'] = nota3_nuevo
                         estudiantes.append(cedulas)
                         print(f"ACTUALIZASTE TU NOTA3, EXITOSAMENTE!")
                         break
                        else: print("Dato invalido, ingresa solo numeros")

        if boolean == False:
           print(f"Dato invalido : {cedula_estudiante_actualizacion} no apareces en nuestro sistema, registrate en la opcion 4")
        
    
                

    elif opcion == 4:
        print("Ingresa tu numero de cedula para confirmar la eliminacion en matricula")
        cedula_ingresada = input("formato requerido ej: 19.726.926: ")
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