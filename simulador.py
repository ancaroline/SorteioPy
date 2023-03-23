from typing import List, Dict
from time import sleep
import random
import numpy

from models.cartao import Cartao


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
    print('Random Numbers')
    print('===============')

    cartao = Cartao([], [])

    def select_random(aleatory: List) -> List:
        return numpy.random.choice(aleatory, 20, False)

    print(select_random(cartao.num_cartao()))


def numeros_tecnica() -> None:
    pass


def escolher_numeros() -> None:
    pass


def verificar_acertos() -> None:
    pass


def limpar_simulador() -> None:
    pass


if __name__ == '__main__':
    main()
