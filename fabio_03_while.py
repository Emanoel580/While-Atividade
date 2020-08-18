# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.
def main():
    A0 = int(input("primeiro termo: "))
    Limite = int(input("ultimo termo: "))
    R = int(input("razão: "))
    cont = 1

    while cont < Limite:
        print(cont)
        cont += R

main()
