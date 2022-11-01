class Rectangulo:

  """
  Crear una clase  llamada rectangulo, debe tener 2 atributos:
  Altura y base el nombre del método será calcular area utilizando la formula.
  Area = base * altura, pero la base y la altura deben ser ingresados por el usuario y los objetos deben ser 3 resultados"
"""
class Rectangulo:
    def  __init__(self, altura, base):
     self. altura= altura
     self.base= base
    def calcular_area (self):
        return self.altura * self.base

base= int(input(f'Digite el numero para la base del rectangulo: '))
altura= int(input('Digite el numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo (base,altura)
print(f" El area es: {rectangulo1.calcular_area()}")

