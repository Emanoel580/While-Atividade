# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.
def main():
    A0 = int(input("primeiro termo: "))
    Limite = int(input("limite: "))
    R = int(input("razão: "))
    Pg(A0, Limite, R)

def Pg (A0, Limite, R):
    cont = 1
    while Limite > (A0 * R ** (cont - 1)):
        print(A0 * R ** (cont - 1))
        cont += 1


main()
