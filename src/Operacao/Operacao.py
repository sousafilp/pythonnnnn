from datetime import date


class Operacao:
    def __init__(self, cpf: str, codigo: int):
        self._data = date.today()
        self._cpf = cpf
        self._codigo = codigo
        self._ativo = False

    def set_data(self, data: date):
        self._data = data

    def get_data(self):
        return self._data

    def set_cpf(self, cpf: str):
        self._cpf = cpf

    def get_cpf(self):
        return self._cpf

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_ativo(self, ativo: bool):
        self._ativo = ativo

    def is_ativo(self):
        return self._ativo
