x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if x > y:
    z = x
    x = y
    y = z

impar = x

if impar%2 == 0:
    impar += 1 

while impar <= y:
    print(impar)
    impar += 2