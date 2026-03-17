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
cp11 = 7
cp12 = 1
sp11 = 9
sp12 = 1
gs11 = 9

# semestre 2
cp21 = 4
cp22 = 0
sp21 = 5
sp22 = 4
gs22 = 10

m1 = ((cp11 + cp12) / 2) * 0.2 + (sp11 + sp12) * 0.1 + gs11 * 0.6
m2 = ((cp21 + cp22) / 2) * 0.2 + (sp21 + sp22) * 0.1 + gs22 * 0.6
mf = m1 * 0.4 + m2 * 0.6

if mf < 6:
    re = f"Vc perdeu de ano, sua nota foi {mf}"
else:
    re = f"Parabens vc passou de ano, sua nota foi {mf}"

print(" ")
print(re)