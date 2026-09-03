import pandas as pd

class Carros:
    def __init__(self, marca, modelo, ano, tipo, cor):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.cor = cor
        self.ano = ano


carro1 = Carros("Chevrolet", "Onix", 1999, "Hatch", "Preto")
carro2 = Carros("Fiat", "Argo", 2021, "Hatch", "Branco")
carro3 = Carros("Volkswagen", "Nivus", 2022, "SUV", "Prata")

Carros = {
   'Carro 1': carro1.__dict__,
   'Carro 2': carro2.__dict__,
   'Carro 3': carro3.__dict__
}

print(Carros)

df = pd.DataFrame(Carros)
print(df)

def clas(ano):
    if ano < 2000:
        return "Antigo"
    else:
        return "Recente"

df.loc['Classificação'] = df.loc['ano'].apply(clas)
df.bas

print(df)