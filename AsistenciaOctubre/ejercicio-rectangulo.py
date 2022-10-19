#Hecho por Damian Quiñonez - WorkBots

# Fin ejercicio realizado por Damian Quiñonez

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Alumno: Facundo Giuliano

# Ejercicio: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario donde
# la clave sea el nombre del usuario y el valor sea el telefono, el programa tendra el siguiente menu:
#     1. Nuevo contacto
#     2. Borrar contacto
#     3. Ver contactos existentes
#     4. Salir

agenda = {}
while True:
    print("\t.:Menu:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente")
        else:
            print("El contacto ya existe")
    elif opcion == 2:
        nombre = input("Cual es el nombre del contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("El contacto se a eliminado.")
        else:
            print("El contacto no existe")
    elif opcion == 3:
        print("Agenda de contactos: ")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por usar su agenda de contactos")
        break
    else:
        print("Se equivoco de opcion.")
        print()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

