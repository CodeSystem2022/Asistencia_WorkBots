#Ejercicio N3: Rectangulo en python
#Alumno: Quiñonez Nelson Damián

class Rectangulo:
    def __init__(self, altura, base, color):
        self.__altura= altura
        self.__base= base
        self.__color= color

    # Getters: empleamos para obtener los datos
    def get_altura(self):
        print(f'Altura: {self.__altura}')

    def get_base(self):
        print(f'Base: {self.__base}')
    
    def get_color(self):
        print(f'Color: {self.__color}')

    def get_caract(self):
        print(f'Altura: {self.__altura}')
        print(f'Base: {self.__base}')
        print(f'Color: {self.__color}')

    # Setters: se emplea para cambiar el valor de los datos
    def set_altura(self, n_altura):
        self.__altura= n_altura
    
    def set_base(self, n_base):
        self.__base= n_base
    
    def set_color(self, n_color):
        self.__color= n_color
    
rect1= Rectangulo(78, 195, 'verde')

rect2= Rectangulo(64, 72, 'amarillo')

rect3= Rectangulo(53, 78, 'rojo')

# Mostrar caracteristicas particulares de cada objeto.
rect1.get_altura()
rect2.get_base()
rect3.get_color

#Mostramos todas las caracteristicas de un objeto.
rect1.get_caract()

#Cambiamos las caracteristicas
rect1.set_color('rojo')

#Mostramos los cambios
rect1.get_color()


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

# Alumna Vilma Jara - Asistencia Octubre 2022

class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad


ancho = int(input('Digite el ancho del cubo: '))
altura = int(input('Digite la altura del cubo: '))
profundidad = int(input('Digite la profundidad del cubo: '))

cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Alumno: Ferro P. Nicolás

class Cubo:
    """
    Crear la clase cubo con los atributos, ancho alto y profundidad, con
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad.
    que el usuario ingrese los valores.
    """

    def __init__(self,altura, base, prof):
        self.altura = altura
        self.base = base
        self.prof = prof

    def calcular_volumen(self):
        return self.altura * self.base * self.prof

base = int(input('Digite el numero de a base del cubo: '))
altura = int(input('Digite un numero de altura para el cubo: '))
prof= int(input('Digite un numero para la altura del cubo: '))
cubo1 = Cubo(base, altura,prof)
print(f'EL area del cubo es: {cubo1.calcular_volumen()}')


#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumno:Manrique Cristian Fernando
class Cubo:
    """"
    Ejercicio para  asistencia LABORATORIO II, PROGRAMACIÓN II: MANRIQUE CRISTIAN FERNANDO
    El ejercicio es crear la clase Cubo con los atributos, alto, ancho, profundidad, 
    con un metodo que llame calcular_volumen que tendra la formula:
    (volumen = ancho * altura * profundidad)
    Y que el usuario ingrese los valores manual.
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

alto = int(input(f"Digite el numero para el alto del cubo: "))
ancho = int(input(f"Digite el numero para el ancho del cubo: "))
profundidad = int(input(f"Digite el numero para la profundidad del cubo: "))

cubo1 = Cubo(alto, ancho, profundidad)

print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")
