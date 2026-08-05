# Victor Paes Pontes - RM 572781
# Sávio Pessôa Afonso - RM 570789

tarifaBase = 2.5

erro = "\nInsira uma opção válida (1 à 4) !"

cp = int (input('\nCalculadora de Tarifas de Transporte, bem vindo !\n1 - Estudante \n2 - Trabalhador \n3 - Idoso \n4 - Comum \nOpção: '))

while cp >= 1 and cp <= 4:
    cp = int (input('\nCalculadora de Tarifas de Transporte, bem vindo !\n1 - Estudante \n2 - Trabalhador \n3 - Idoso \n4 - Comum \nOpção: '))
    print(erro)

distancia = float(input('\nInsira a distância que percorreu (em KM): '))

if distancia <= 0  or distancia == None:
    print('\nInsira um valor de verdade para a distância !')
else:
    match cp:
        case 1:
            total = (tarifaBase * distancia) * 0.5
            categoria = "Estudante"
        case 2:
            total = (tarifaBase * distancia) * 0.8
            categoria = "Trabalhador"
        case 3:
            total = 0
            categoria = "Idoso"
        case 4:
            total = (tarifaBase * distancia)
            categoria = "Comum"
        case _:
            print(erro)

print(f'\n Sua categoria é {categoria} e vc percoreo {distancia}km, o valor é de R${total:0.2f}')