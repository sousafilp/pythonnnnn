from src.Operacao.Operacao import Operacao


class Locacao(Operacao):
    def __init__(self, cpf: str, codigo: int, periodo: int):
        super().__init__(cpf, codigo)
        self._periodo = periodo

    def set_periodo(self, periodo: int):
        self._periodo = periodo

    def get_periodo(self):
        return self._periodo
