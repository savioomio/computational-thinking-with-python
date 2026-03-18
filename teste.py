# print(" ")
# print("Notas do Primeiro semestre")
# cp11 = float(input("Checkpoint 1: "))
# cp12 = float(input("Checkpoint 2: "))
# sp11 = float(input("Sprint 1: "))
# sp12 = float(input("Sprint 2: "))
# gs11 = float(input("Global Solution: "))

# print(" ")
# print("Notas do Segundo semestre")
# cp21 = float(input("Checkpoint 1: "))
# cp22 = float(input("Checkpoint 2: "))
# sp21 = float(input("Sprint 1: "))
# sp22 = float(input("Sprint 2: "))
# gs22 = float(input("Global Solution: "))

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

cps1.remove(min(cps1))
cps2.remove(min(cps2))
# print(f"Checkpoint Maiores {cps1}, {cps2}")

cps1Soma = sum(cps1)
cps2Soma = sum(cps2)
# print(f"Checkpoint Soma, Semestre 1: {cps1Soma}, Semestre 2: {cps2Soma}")

m1 = (cps1Soma / 2) * 0.2 + (sp11 + sp12) * 0.1 + gs11 * 0.6
m2 = (cps2Soma / 2) * 0.2 + (sp21 + sp22) * 0.1 + gs22 * 0.6
mf = m1 * 0.4 + m2 * 0.6

if mf >= 6:
    re = f"Parabens vc passou de ano, sua nota foi {mf} 👌"
else:
    re = f"Vc perdeu de ano, sua nota foi {mf}"

print(" ")
print(re)