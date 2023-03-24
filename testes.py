from models.cartao import Cartao, Numeros
from typing import List, Dict
from time import sleep
import random
import numpy

"""num = [1, 2, 3, 4]
numeros1 = Cartao(num, [1, 2, 3])
print(numeros1)
print(numeros1.num_cartao())"""
num_cartao = []

check: str = input("Você gostaria de utilizá-los neste momento? (y/n)")
if check == 'n':
    quant: int = int(input("Quantos números, contidos no seu cartão, você deseja verificar?"))

    if quant == 3:
        while quant < 4:
            quant -= 1
            if quant == -1:
                break
            else:
                n: int = int(input("Digite os seus números: "))
                num_cartao.append(n)
                print(num_cartao)

        num_sort: List = []
        for n1 in range(3):
            n1: int = int(input('Digite os números sorteados: '))
            num_sort.append(n1)
            print(num_sort)

        # Verificando se num_cartao está dentro de num_sort
        cont = 0
        for elem in num_sort:
            if elem in num_cartao:
                cont = cont + 1
        print(f"Você obteve {cont} acerto(s).")