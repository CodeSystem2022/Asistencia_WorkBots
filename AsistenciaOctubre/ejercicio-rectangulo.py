class Rectangulo:
    def __init__(self, altura, base, color):
        self.__altura= altura
        self.__base= base
        self.__color= color

    # Getters
    def get_altura(self):
        print(f'Altura: {self.__altura}')

    def get_base(self):
        print(f'Base: {self.__base}')
    
    def get_color(self):
        print(f'Color: {self.__color}')

    def get_caracteristicas(self):
        print(f'Altura: {self.__altura}')
        print(f'Base: {self.__base}')
        print(f'Color: {self.__color}')

    # Setters
    def set_altura(self, n_altura):
        self.__altura= n_altura
    
    def set_base(self, n_base):
        self.__base= n_base
    
    def set_color(self, n_color):
        self.__color= n_color
    
r1= Rectangulo(124, 241, 'azul')

r2= Rectangulo(16, 24, 'rojo')

r3= Rectangulo(53, 78, 'negro')

# Mostrar caracteristicas particulares de cada objeto.
r1.get_altura()
r2.get_base()
r3.get_color

# Mostrar todas las caracteristicas de un objeto.
r1.get_caracteristicas()

# Cambiar caracteristicas
r1.set_color('blanco')

# Mostrar cambios
r1.get_color()
