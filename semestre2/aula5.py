# Usanso POO (Programação Orientada a Objetos) em Python calucule a area e perimetro de um retangulo
import pandas as pd

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    

retangulo1 = Retangulo(5, 10)
retangulo2 = Retangulo(6, 6)
retangulo3 = Retangulo(5, 4)
retangulo4 = Retangulo(6, 6)
retangulo5 = Retangulo(1, 8)

lista_retangulos = [retangulo1, retangulo2, retangulo3, retangulo4, retangulo5]

for i, retangulo in enumerate(lista_retangulos):
    lista_retangulos[i] = {
        "nome": f"Retângulo {i+1}",
        "área": retangulo.area(),
        "perímetro": retangulo.perimetro()
    }

df = pd.DataFrame(lista_retangulos)
print(df)