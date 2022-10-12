# Programa que modifica el archivo agenda.txt
# Programa que modifica el archivo agenda.txt
 
 
while True: # Bucle infinito
    opcion = input("""
    Programa que modifica el archivo agenda.txt
    Seleccione una opción:
        1. Agregar persona
        2. Modificar persona
        3. Eliminar persona
        4. Salir
    """) # Selecciona una opción
    if opcion == "1": # Agregar persona
        # Formulario que solicita nombre y apellido de una persona y luego pregunta su edad, telefono y correo electronico.
        personas = [] # Lista vacia para almacenar los datos de las personas
        while True: # Bucle infinito
            # Solicitamos nombre y apellido y los guardamos en una variable
            nombre = input("Introduce un nombre: ").capitalize()
            apellido = input("Introduce su apellido: ").capitalize()
            persona = [nombre , apellido]  # Guardamos los datos en una lista
            while True:
                try : # Intentamos convertir la edad en un entero
                    telefono = input("Introduce su teléfono (Solo números): ")
                    int(telefono) # No vamos a guardar el teléfono como un número ya que podríamos perder datos. Esta línea solo sirve para comprobar si es un número. Si no lo es, manda un error
                    persona.append(telefono) # Agregamos el teléfono a la lista pequeña (persona)
                    break
                except ValueError: # Si introduce algo que no sea un número muestra un mensaje de error y vuelve a pedir el número telefónico
                    print("Error, debes ingresar un número para tu teléfono")
            # Pedimos el correo electronico y lo guardo en una variable
            correo = input("Introduce su correo: ") # Guardamos el correo en una variable
            persona.append(correo) # Agregamos el correo a la lista pequeña (persona)
            # Agregamos la persona a la lista de personas
            personas.append(persona) # Agregamos la lista pequeña (persona) a la lista grande (personas)
            print("Persona agregada") # Mostramos un mensaje de que la persona fue agregada
            break # Continuamos con el programa
        f_archivo = open("agenda.txt", "a") # Abrimos el archivo en modo de escritura (append)
        for contacto in personas: # Recorremos la lista de personas
            # Guardamos los datos de cada persona en el archivo indicando su nombre, apellido telefono y correo
            f_archivo.write(contacto[0] + " " + contacto[1] + ": Teléfono: " + str(contacto[2]) + " e-mail: " + contacto[3] + "\n")
        f_archivo.close() # Cerramos el archivo
        input("Datos guardados\nPresione una tecla para continuar")
 
    elif opcion == "2": # Modificar persona
        f_nuevo1 = open("agenda.txt", "r") # Abrimos el archivo en modo lectura
        contactos = f_nuevo1.readlines() # Leemos todas las lineas del archivo y las guardamos en una lista
        f_nuevo1.close() # Cerramos el archivo
        while True:
            contador = 1 # Contador para mostrar los contactos
            for contacto in contactos:
                print(contador, contacto) # Mostramos los contactos con un contador
                contador += 1 # Aumentamos el contador
            try: # Intentamos convertir el número de contacto en un entero
                numero = int(input('Seleccione el número de contacto a modificar: ')) # Pedimos el número de contacto a modificar
 
            except ValueError: # Si no es un número, mostramos un mensaje de error y volvemos a pedir el número de contacto
                print('Error, debe ingresar un número')
            if numero > len(contactos) or numero < 1:
                print('Error, el número de contacto no existe')
            else: # Si el número de contacto es correcto, mostramos el contacto y preguntamos si desea modificarlo
                contacto = contactos[numero - 1] # Guardamos el contacto en una variable
                contacto = contacto.split(': ') # Separamos el contacto en una lista cada vez que encuentre ': '
                nombre = contacto[0].replace(' Teléfono', '') # Guardamos el nombre y apellido en una variable, sin el string ' Teléfono'
                telefono = contacto[2].replace(' e-mail', '') # Guardamos el teléfono en una variable, sin el string 'e-mail'
                correo = contacto[3].replace('\n', '') # Guardamos el correo en una variable, sin el string '\n'
                print('-1. Nombre: ', nombre) # Mostramos el nombre y apellido
                print('-2. Teléfono: ', telefono) # Mostramos el teléfono
                print('-3. e-mail: ', correo) # Mostramos el correo
                print('-4. Salir') # Mostramos la opción de salir
                while True:
                    try:
                        modificar = int(input('Seleccione la opción a modificar: ')) # Pedimos la opción a modificar
                        break
                    except ValueError:
                        print('Error, debe ingresar un número')
                if modificar == 1:
                    nombre = input("Introduce tu nombre: ").capitalize() # Pedimos el nombre y lo guardamos en una variable
                    apellido = input("Introduce tu apellido: ").capitalize() # Pedimos el apellido y lo guardamos en una variable
                    contactos[numero - 1] = nombre + ' ' + apellido + ' Teléfono: ' + telefono + ' e-mail: ' + correo + '\n' # Guardamos el contacto con los datos modificados
                    input('Nombre modificado\nPresione una tecla para continuar') # Mostramos un mensaje de que el nombre fue modificado 
                elif modificar == 2: # Si la opción es 2, pedimos el nuevo teléfono
                    while True:
                        try:
                            telefono = int(input('Ingrese el nuevo teléfono: ')) # Pedimos el nuevo teléfono y lo guardamos en una variable
                            contactos[numero - 1] = nombre + ' Teléfono: ' + str(telefono) + ' e-mail: ' + correo + '\n' # Guardamos el contacto con los datos modificados
                            print('Teléfono modificado') # Mostramos un mensaje de que el teléfono fue modificado
                            break
                        except ValueError:
                            print('Error, debe ingresar un número')
                elif modificar == 3: # Si la opción es 3, pedimos el nuevo correo
                    correo = input('Ingrese el nuevo correo: ') # Pedimos el nuevo correo y lo guardamos en una variable
                    contactos[numero - 1] = nombre + ' Teléfono: ' + telefono + ' e-mail: ' + correo + '\n' # Guardamos el contacto con los datos modificados
                    print('Correo modificado')
                elif modificar == 4: # Si la opción es 4, salimos del programa
                    break
                else:
                    print('Error, la opción no existe') # Si la opción no existe, mostramos un mensaje de error
                f_nuevo2 = open("agenda.txt", "w") # Abrimos el archivo en modo escritura
                for contacto in contactos: # Recorremos la lista de contactos
                    f_nuevo2.write(contacto) # Guardamos cada contacto en el archivo
                f_nuevo2.close() # Cerramos el archivo
                print('Datos modificados') # Mostramos un mensaje de que los datos fueron modificados
                break # Salimos del bucle
  
    elif opcion == "3": # Eliminar persona
        f_nuevo1 = open("agenda.txt", "r") # Abrimos el archivo en modo lectura
        contactos = f_nuevo1.readlines() # Leemos todas las lineas del archivo y las guardamos en una lista
        contador = 1 # Contador para mostrar los contactos
        while True: # Bucle para mostrar los contactos
            for contacto in contactos: # Recorremos la lista de contactos
                print(contador, contacto) # Mostramos los contactos con un contador
                contador += 1 # Aumentamos el contador
            try: # Intentamos convertir el número de contacto en un entero
                opcion = int(input('Seleccione el número de contacto a eliminar: ')) 
                break
            except ValueError: # Si no es un número, mostramos un mensaje de error y volvemos a pedir el número de contacto
                print('Error, debe ingresar un número') 
        if opcion > len(contactos) or opcion < 1: # Si el número de contacto es incorrecto, mostramos un mensaje de error
            input('Error, el número de contacto no existe')
        else: # Si el número de contacto es correcto, mostramos el contacto y preguntamos si desea eliminarlo
            contactos.pop(opcion - 1) # Eliminamos el contacto de la lista
            f_nuevo2 = open("agenda.txt", "w") # Abrimos el archivo en modo escritura
            for contacto in contactos:  # Recorremos la lista de contactos
                f_nuevo2.write(contacto) # Guardamos cada contacto en el archivo
            f_nuevo2.close() # Cerramos el archivo
            print('Datos eliminados') # Mostramos un mensaje de que los datos fueron eliminados
 
    elif opcion == "4": # Salir
        print('Gracias por usar la agenda') # Mostramos un mensaje de despedida
        break # Salimos del bucle
   
    else: # Si la opción no existe, mostramos un mensaje de error
        print('Elige una opción válida') # Mostramos un mensaje de error
