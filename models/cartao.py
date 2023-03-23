from typing import List, Dict
from models.numeros import Numeros


class Cartao(Numeros):

    def __init__(self, numeros_totais: List, numeros_selecionados: List) -> None:
        super().__init__(numeros_totais)
        self.__numeros_selecionados = numeros_selecionados

    @property
    def numeros_selecionados(self) -> List:
        return self.__numeros_selecionados

    def __str__(self) -> str:
        return f'Jogue os Números: {self.__numeros_selecionados}'
