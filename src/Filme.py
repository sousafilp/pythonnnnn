from datetime import date


class Filme:
    def __init__(self, codigo: int, titulo: str):
        self._codigo = codigo
        self._titulo = titulo
        self._genero = []
        self._data_lancamento = date
        self._diretor = ''
        self._atores = []
        self._sinopse = ''
        self.produtores = []
        self.preco_locacao = float()
        self.numero_copias = int()

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def get_titulo(self):
        return self._titulo

    def set_genero(self, genero: str):
        self._genero.append(genero)

    def get_genero(self):
        return self._genero

    def add_genero(self, genero: str):
        pass

    def set_data_lancamento(self, data_lancamento: date):
        self._data_lancamento = data_lancamento

    def get_data_lancamento(self):
        return self._data_lancamento

    def set_diretor(self, diretor: str):
        self._diretor = diretor

    def get_diretor(self):
        return self._diretor

    def set_atores(self, atores: list):
        self._atores.append(atores)

    def get_atores(self):
        return self._atores

    def add_ator(self, ator: str):
        self._atores
