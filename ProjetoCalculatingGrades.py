# print(" ")
# print("Notas do Primeiro semestre")
# cps1 = []
# for i in range(3):
#     checkpointS1 = float(input(f"Checkpoint {i+1}: "))
#     cps1.append(checkpointS1)
#
# sp11 = float(input("Sprint 1: "))
# sp12 = float(input("Sprint 2: "))
# gs11 = float(input("Global Solution: "))
#
# print(" ")
# print("Notas do Segundo semestre")
# cps2 = []
# for i in range(3):
#     checkpointS2 = float(input(f"Checkpoint {i+1}: "))
#     cps2.append(checkpointS2)
#
# sp21 = float(input("Sprint 1: "))
# sp22 = float(input("Sprint 2: "))
# gs22 = float(input("Global Solution: "))
#
# fq = float( input("Frequencia: "))

# semestre 1
cps1 = [2, 4, 10]
sp11 = 9
sp12 = 1
gs11 = 9

# semestre 2
cps2 = [5, 8, 10]
sp21 = 5
sp22 = 4
gs22 = 10

fq = 0.76

cps1.remove(min(cps1))
cps2.remove(min(cps2))
# print(f"Checkpoint Maiores {cps1}, {cps2}")

cps1Soma = sum(cps1)
cps2Soma = sum(cps2)
# print(f"Checkpoint Soma, Semestre 1: {cps1Soma}, Semestre 2: {cps2Soma}")

m1 = (cps1Soma / 2) * 0.2 + (sp11 + sp12) * 0.2 + gs11 * 0.6
m2 = (cps2Soma / 2) * 0.2 + (sp21 + sp22) * 0.2 + gs22 * 0.6
mf = m1 * 0.4 + m2 * 0.6

if fq <= 0.75:
    re = f"PERDEU POR FREQUENCIA: perdeu direto por conta da frequencia {fq:.0%}"
elif mf >= 6:
    re = f"PASSOU, sua nota foi {mf:.2f} e fua frequencia foi {fq:.0%}"
elif mf >= 4:
    re = f"EXAME: sua nota foi {mf:.2f} e fua frequencia foi {fq:.0%}"
else:
    re = f"PERDEU, sua nota foi {mf:.2f} e fua frequencia foi {fq:.0%}"

print(" ")
print(re)