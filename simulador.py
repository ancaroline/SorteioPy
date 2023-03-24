from typing import List, Dict
from time import sleep
import random
import numpy

from models.cartao import Cartao

num_cartao = []
num_selecionados = []


def main() -> None:
    menu()


def menu() -> None:
    print('======================')
    print('==== Bem-vindo(a) ====')
    print('======================')

    print('Selecione uma opção abaixo: ')
    print('1 - 20 números aleatórios')
    print('2 - 20 números a partir da Técnica Secreta')
    print('3 - Escolher números para compor a Técnica Secreta')
    print('4 - Verificar acertos')
    print('5 - Limpar simulador')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        numeros_aleatorios()
    elif opcao == 2:
        numeros_tecnica()
    elif opcao == 3:
        escolher_numeros()
    elif opcao == 4:
        verificar_acertos()
    elif opcao == 5:
        limpar_simulador()
    elif opcao == 6:
        print('Boa sorte em seu sorteio!')
        sleep(2)
        exit()
    else:
        print('Opção inválida.')
        sleep(1)
        menu()


def numeros_aleatorios() -> None:
    print('20 Números Aleatórios Selecionados')
    print('==================================')

    cartao = Cartao([], [])

    def select_random(aleatory: List) -> List:
        return numpy.random.choice(aleatory, 20, False)

    # falta colocar os números em ordem crescente
    print(select_random(cartao.num_cartao()))
    sleep(2)
    menu()


def numeros_tecnica() -> None:
    pass


def escolher_numeros() -> None:
    pass


def verificar_acertos() -> None:
    print('Verificando Acertos')
    print('====================')
    sleep(1)
    print("Você já possui números no sistema?")
    sleep(1)
    check: str = input("Você gostaria de utilizá-los neste momento? (y/n)")
    if check == 'n':
        quant: int = int(input("Quantos números, contidos no seu cartão, você deseja verificar?"))

        # Quantidade
        if quant == 50:
            while quant < 51:
                quant -= 1
                if quant == -1:
                    break
                else:
                    n: int = int(input("Digite os seus números: "))
                    num_cartao.append(n)
                    print(num_cartao)

            num_sort: List = []
            for n1 in range(20):
                n1: int = int(input('Digite os números sorteados: '))
                num_sort.append(n1)
                print(num_sort)

            # Verificando se num_cartao está dentro de num_sort
            cont = 0
            for elem in num_sort:
                if elem in num_cartao:
                    cont = cont + 1
            print(f"Você obteve {cont} acerto(s).")
            sleep(3)
            menu()
        else:
            print("Este valor não é suportado.")
            sleep(2)
            menu()
    else:
        pass


def limpar_simulador() -> None:
    pass


if __name__ == '__main__':
    main()
