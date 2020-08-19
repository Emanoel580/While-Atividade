# Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.
limite_inferior = int(input('inferior: '))
limite_superior = int(input('superior: '))
cont = 1

while cont < limite_superior:
    if limite_inferior % 2 == 0:
        print(cont, end=' ')
        cont =+ 1

