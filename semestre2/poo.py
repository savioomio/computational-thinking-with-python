# Usanso POO (Programação Orientada a Objetos) em Python calucule a area e perimetro de um retangulo

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo1 = Retangulo(5, 10)
print("Área do retângulo:", retangulo1.area())