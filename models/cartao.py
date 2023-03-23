from typing import List, Dict
from models.numeros import Numeros


class Cartao(Numeros):

    def __init__(self, numeros_totais: Numeros, numeros_selecionados: List) -> None:
        super().__init__(numeros_totais)
        self.__numeros_selecionados = numeros_selecionados

    @property
    def numeros_selecionados(self) -> List:
        return self.__numeros_selecionados

    def __str__(self) -> str:
        return f'Números do cartão: {self.num_cartao()}' \
               f'\nJogue os Números: {self.numeros_selecionados}'\
