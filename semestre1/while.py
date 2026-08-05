"""
n = 1
total = 0

while n <= 15:
    ni = int(input(f"vc tem que fornecer 15 numeros impares, vc ja me deu {n} numeros: "))
    if ni%2 != 0:
        total += ni    
    n += 1

print(f"total: {total}")
"""

n = -1
total = 0

while n != 0:
    n = int(input(f"Digite alguns numeros: "))
    total += n 

print(f"total: {total}")