from datetime import date


class Filme:
    def __init__(self, codigo: int, titulo: str):
        self._codigo = codigo
        self._titulo = titulo
        self._generos = []
        self._data_lancamento = date.today()
        self._diretor = str()
        self._atores = []
        self._sinopse = str()
        self._produtores = []
        self._preco_locacao = float()
        self._numero_copias = int()

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def get_titulo(self):
        return self._titulo

    def set_genero(self, genero: list):
        self._generos = genero

    def get_genero(self):
        return self._generos

    def add_genero(self, genero: str):
        self._generos.append(genero)

    def set_data_lancamento(self, data_lancamento: date):
        self._data_lancamento = data_lancamento

    def get_data_lancamento(self):
        return self._data_lancamento

    def set_diretor(self, diretor: str):
        self._diretor = diretor

    def get_diretor(self):
        return self._diretor

    def set_atores(self, atores: list):
        self._atores = atores

    def get_atores(self):
        return self._atores

    def add_ator(self, ator: str):
        self._atores.append(ator)

    def set_sinopse(self, sinopse: str):
        self._sinopse = sinopse

    def get_sinopse(self):
        return self._sinopse

    def set_produtores(self, produtores: list):
        self._produtores = produtores

    def get_produtores(self):
        return self._produtores

    def add_produtor(self, produtor: str):
        self._produtores.append(produtor)

    def set_preco_locacao(self, preco_locacao: float):
        self._preco_locacao = preco_locacao

    def get_preco_locacao(self):
        return self._preco_locacao

    def set_numero_copias(self, numero_copias: int):
        self._numero_copias = numero_copias

    def get_numero_copias(self):
        return self._numero_copias

    def imprimir(self):
        print(f"Codigo: {self._codigo}\nTitulo: {self._titulo}\nGenero: {self._generos}\nData de Lancamento: "
              f"{self._data_lancamento}\nAtores: {self._atores}\nDiretor: {self._diretor}\nSinopse: {self._sinopse}")
