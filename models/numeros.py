from typing import List, Dict


class Numeros:

    def __init__(self, numeros_totais: List):
        self.__numeros_totais = numeros_totais

    @property
    def numeros_totais(self) -> List:
        return self.__numeros_totais

    def num_cartao(self) -> List:
        numeros_totais = []
        for n in range(1, 101):
            numeros_totais.append(n)
        return numeros_totais

    """def __str__(self) -> str:
        return f'Números totais: {self.numeros_totais}'"""


"""
    def numeros_fileiras(self):
        fileira1 = []
        for n in range(1, 11):
            fileira1.append(n)

        fileira2 = []
        for n in range(11, 21):
            fileira2.append(n)

        fileira3 = []
        for n in range(21, 31):
            fileira3.append(n)

        fileira4 = []
        for n in range(31, 41):
            fileira4.append(n)

        fileira5 = []
        for n in range(41, 51):
            fileira5.append()

        fileira6 = []
        for n in range(51, 61):
            fileira6.append()

        fileira7 = []
        for n in range(61, 71):
            fileira7.append()

        fileira8 = []
        for n in range(71, 81):
            fileira8.append()

        fileira9 = []
        for n in range(81, 91):
            fileira9.append()

        fileira10 = []
        for n in range(91, 101):
            fileira10.append()"""
