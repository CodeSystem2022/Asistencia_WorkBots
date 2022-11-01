# ALUMNO : FACUNDO LEONEL CANO
# ASISTENCIA DE OCTUBRE 2021

"""
# Crear una clase  llamada {Rectangulo} y tiene que tener 2 atributos:
# La Altura y la Base
# El método o Formula que vamos a utilizar para calcular el Area del Rectangulo es la siguiente:
# Area = Base * Altura
# La Base y la Altura los tiene que ingresar el usuario"
"""

# {EJERCICIO - RECTANGULO}

class Rectangulo:

    def __init__(self, Altura, Base):
        self.Altura = Altura
        self.Base = Base

    def Calcular_Area(self):
        return self.Altura * self.Base


Base = int(input('Digite un numero para darle un valor a la base del Rectangulo: '))

Altura = int(input('Digite un numero para darle un valor a la altura del Rectangulo: '))

CalculoDelRectangulo = Rectangulo(Base, Altura)

print(f" El area del Rectangulo es: {CalculoDelRectangulo.Calcular_Area()}")
