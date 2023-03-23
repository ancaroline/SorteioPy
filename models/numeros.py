from typing import List, Dict


class Numeros:

    def __init__(self, numeros_totais: List):
        self.__numeros_totais = numeros_totais

    @property
    def numeros_totais(self) -> List:
        return self.__numeros_totais
