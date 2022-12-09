#-----------------------------------------------------------------------------------------------------------------------------------------------

# Alumno: Facundo Giuliano

# Leccion 12 - Clase -15- POO Parte 8 -Diseño de Clases y Sobrecarga de Operadores-

class Persona:
    def __init__(self, nombre, edad, comidasFavoritas):
        self.nombre = nombre
        self.edad = edad
        self.comidasFavoritas = comidasFavoritas

    def __add__(self, other):  # suma, otro
        return f"{self.nombre} {other.nombre} {self.comidasFavoritas} {other.comidasFavoritas}"

    def __sub__(self, otro): #  resta
        return self.edad - otro.edad


persona1 = Persona("Facundo", 27, ["manzana", "pera"])
persona2 = Persona("Giuliano", 1, ["frutilla", "ciruela"])

#  persona1.__add__(persona2) Sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)
print(persona1.comidasFavoritas + persona2.comidasFavoritas)

a = 3
b = 5
print(a + b)

a = "Hola "
b = "Mundo"
print(a + b)


a = [3, 4, 5]
b = [6, 7, 8, 9]
print(a + b)

# miObjeto1 + miObjeto2 = esto no se puede hacer

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Alumna: Vilma Jara

class Producto:
    contador_productos = 0  # Variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1  # Aumento para la variable de clase
        self._id_producto = Producto.contador_productos  # Asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio

    # Métodos setters and getters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Sobre escribimos el método str
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'


if __name__ == '__main__':  # Solo será visible se la prueba se ejecuta desde aquí
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
..................................................................................................................................................
#Alumna: Leonela Reyes

#Clase 15 POO- Diseño de Clases y Sobrecarga de Operadores.

class Persona:
    def __init__(self, nombre, edad, estaciones):
        self.nombre = nombre
        self.edad = edad
        self.estaciones= estaciones
    def __add__(self, other): # sumar
       return f'{self.nombre} {other.nombre} {self.estaciones} {other.estaciones}'

    def __sub__(self, otro):
        return self.edad - otro.edad


persona1 = Persona('Leonela', 28, ['verano',  'invierno'])
persona2 = Persona('Reyes', 11, ['primavera', 'otoño'])

# persona1.__add__(persona2) sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)
print(persona1.estaciones + persona2.estaciones)
a = 3
b = 5
print(a + b)

a = 'Hola '
b = 'mundo'
print(a + b)

a = [3, 4, 5]
b = [6, 7, 8, 9]
print(a + b)

# miObjeto1 + miObjeto2 = esto no se podría hacer
..................................................................................................................................................
#Alumno: Ferro P Nicolás

#Clase 15 POO. Diseño de clases y sobrecarga de operadores.

class Persona:
    def __init__(self, nombre, edad, estaciones):
        self.nombre = nombre
        self.edad = edad
        self.estaciones= frutas
    def __add__(self, other): # sumar
       return f'{self.nombre} {other.nombre} {self.frutas} {other.frutas}'

    def __sub__(self, otro):
        return self.edad - otro.edad


persona1 = Persona('Nico', 29, ['Durazno',  'Sandia'])
persona2 = Persona('Dani', 29, ['Melon', 'Kiwi'])

# persona1.__add__(persona2) sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)
print(persona1.frutas + persona2.frutas)
a = 3
b = 5
print(a + b)

a = 'Hola '
b = 'mundo'
print(a + b)

a = [3, 4, 5]
b = [6, 7, 8, 9]
print(a + b)

# miObjeto1 + miObjeto2 = esto no se podría hacer


#------------------------------------------------------------------------------------------------------------------------------------------------
# Alumno: Manrique Cristian

" Asistencia Noviembre

# Class persona

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):  # Other = otro
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, otro):  # Sub = substraction (resta)
        return self.edad - otro.edad


persona1 = Persona('Natalia', 38)
persona2 = Persona('Gonzalez', 5)

# persona1.__add__(persona2) sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)



# ALUMNO: MANRIQUE CRISTIAN
class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color

    def __str__(self):
        return f'Color [color: {self._color}]'
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Alumno: Nelson Damian Quiñonez
# Leccion 11 - Clase 15 POO Parte 8 Diseño de clases y Sobrecarga de Operadores

class Producto:
    contador_productos = 0  # Variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1  # Aumento para la variable de clase
        self._id_producto = Producto.contador_productos  # Asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio

    # Métodos setters and getters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Sobre escribimos el método str
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'


if __name__ == '__main__':  # Solo será visible se la prueba se ejecuta desde aquí
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
    
#------------------------------------------------------------------------------------------------------------------------------------------
    
  # Leccion 12 - Clase 15 POO Parte 8 Diseño de clases y Sobrecarga de Operadores

  # Alumno: FACUNDO LEONEL CANO

class Persona:
    def __init__(self, Nombre, Edad, ComidaFavorita):
        self.Nombre = Nombre
        self.Edad = Edad
        self.ComidaFavorita = ComidaFavorita

    def __add__(self, other):  # Metodo de la (Suma, Otro - Other)
        return f"{self.Nombre} {other.Nombre} {self.ComidaFavorita} {other.ComidaFavorita}"

    def __sub__(self, Otro):  # Metodo de la Resta
        return self.Edad - Otro.Edad

    
  # Ingreso de Datos

Persona1 = Persona("Facundo", 21, ["Sandia", "Naranja"])

Persona2 = Persona("Loenel", 18, ["Granada", "Mandarina"])

  # Persona1.__add__(Persona2) Sintaxis Interna y Automatica

print(f'Datos Importantes'.center(50, '-'))

print(f'Suma de los Objetos: {Persona1 + Persona2}')

print(f'Resta de los Objetos: {Persona1 - Persona2}')

print(f'Suma de las Comidas Favoritas: {Persona1.ComidaFavorita + Persona2.ComidaFavorita}')

