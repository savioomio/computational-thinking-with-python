import pandas as pd

dic = {
    'Ponto A': [10, 20, 30, 40, 50],
    'Ponto B': [100, 200, 300, 400, 500],
    'Ponto C': [1, 2, 3, 4, 5],
}

df = pd.DataFrame(dic)

def clas(a):
    if a < 30:
        return "Baixo"
    elif a < 40:
        return "Médio"
    else:
        return "Alto"

print(df['Ponto A'].apply(clas))