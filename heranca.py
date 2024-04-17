# Definindo a classe base (superclasse)
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses precisam implementar este método")


# Definindo uma subclasse (herança)
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


# Definindo outra subclasse (herança)
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Criando instâncias das subclasses
square = Square("blue", 4)
circle = Circle("red", 3)

# Calculando a área das formas
print("Área do quadrado:", square.area())  # Saída: Área do quadrado: 16
print("Área do círculo:", circle.area())  # Saída: Área do círculo: 28.26
